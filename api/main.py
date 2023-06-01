import os
import random
import re
from typing import Optional
from fastapi import FastAPI, Request, Response, status, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from supabase.client import create_client, Client
from dotenv import load_dotenv
from slowapi.extension import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from deta import Deta

tags_metadata = [
    {
        "name": "Get all jokes",
        "description": "Get an array of all jokes contained in the database. Rate limited to 5 requests per minute.",
    },
    {
        "name": "Get joke by search query",
        "description": "Get a joke by searching for a keyword in the prompt field. Rate limited to 5 requests per minute.",
    },
    {
        "name": "Get a random joke",
        "description": "Get a random joke from the database. Rate limited to 10 requests per minute.",
    },
    {
        "name": "Get joke by id",
        "description": "Get a joke from the database by its id. Rate limited to 10 requests per minute.",
    },
]

load_dotenv()
app = FastAPI(
    title="Deez Nuts Jokes",
    description="The Deez Nuts Jokes API allows users to access a collection of jokes about Deez Nuts to use in their applications. 🥜 The API is powered by Supabase and FastAPI.",
    version="1.0.0",
    contact={
        "name": "DeviousLab",
        "url": "http://deviouslab.dev/",
        "email": "devious@deviouslab.dev",
    },
    license_info={
        "name": "MIT",
        "url": "https://www.mit.edu/~amini/LICENSE.md",
    },
    openapi_tags=tags_metadata,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    docs_url="/",
)
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

url = os.getenv("SUPABASE_SUPAFAST_URL")
key = os.getenv("SUPABASE_SUPAFAST_KEY")
deta = Deta(url)
deta = Deta(key)
supabase: Client = create_client(url, key)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": "Validation error, value is not a valid integer.",
            "body": exc.errors(),
        },
    )


@app.get("/jokes", status_code=status.HTTP_200_OK, tags=["Get all jokes"])
@limiter.limit("5/minute")
def all_jokes(request: Request, max_results: Optional[int] = 47):
    jokes = supabase.table("Jokes").select("*").execute()
    if max_results:
        jokes = supabase.table("Jokes").select("*").limit(max_results).execute()

    return jokes


@app.get("/joke/search", status_code=status.HTTP_200_OK, tags=["Get joke by search query"])
@limiter.limit("5/minute")
def search_jokes(request: Request, response: Response, keyword: Optional[str] = None):
    jokes = supabase.table("Jokes").select("*").execute()
    if keyword:
        query_results = []
        jokes = supabase.table("Jokes").select("*").execute()

        for index in jokes.data:
            if re.search(keyword, index["prompt"], re.IGNORECASE):
                query_results.append(index)
        if not query_results:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No matches found for '{query}'".format(query=keyword),
            )
        return query_results

    return jokes


@app.get("/joke/random", status_code=status.HTTP_200_OK, tags=["Get a random joke"])
@limiter.limit("10/minute")
def random_joke(request: Request):
    random_int = random.randrange(1, 47)
    joke = supabase.table("Jokes").select("*").eq("id", random_int).execute()

    return joke


@app.get("/joke/{dn_id}", status_code=status.HTTP_200_OK, tags=["Get joke by id"])
@limiter.limit("10/minute")
def id_joke(request: Request, response: Response, dn_id: int):
    joke = supabase.table("Jokes").select("*").eq("id", dn_id).execute()
    if not joke.data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No joke found with id {id}".format(id=dn_id),
        )

    return joke
