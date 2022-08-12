import os
import random
import re
from typing import Optional
from fastapi import FastAPI, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from supabase import create_client, Client
from dotenv import load_dotenv
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

tags_metadata = [
    {
        "name": "Get all jokes",
        "description": "Get an array of all jokes contained in the database. Ratelimited to 5 requests per minute.",
    },
    {
        "name": "Get joke by query",
        "description": "Get a joke by searching for a keyword in the prompt field. Ratelimited to 5 requests per minute.",
    },
    {
        "name": "Get a random joke",
        "description": "Get a random joke from the database. Ratelimited to 5 requests per minute.",
    },
    {
        "name": "Get joke by id",
        "description": "Get a joke from the database by its id. Ratelimited to 5 requests per minute.",
    },
]

load_dotenv()
app = FastAPI(
    title="Deez Nuts Jokes",
    description="The Deez Nuts Jokes API allows users to access a collection of jokes about Deez Nuts to use in their applications. 🥜 The API is powered by Supabase and FastAPI.",
    version="0.1.0",
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
    docs_url="/",
)
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

url = os.getenv("SUPABASE_SUPAFAST_URL")
key = os.getenv("SUPABASE_SUPAFAST_KEY")
supabase: Client = create_client(url, key)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Validation error, value is not a valid integer."},
    )


@app.get("/jokes", status_code=status.HTTP_200_OK, tags=["Get all jokes"])
@limiter.limit("5/minute")
def all_jokes(request: Request, max_results: Optional[int] = 47):
    jokes = supabase.table("Jokes").select("*").limit(max_results).execute()

    return jokes


@app.get("/joke/search", status_code=status.HTTP_200_OK, tags=["Get joke by query"])
@limiter.limit("5/minute")
def search_jokes(request: Request, response: Response, keyword: Optional[str] = None):
    if keyword is None:
        return supabase.table("Jokes").select("*").execute()
    else:
        query_results = []
        jokes = supabase.table("Jokes").select("*").execute()

        for index in jokes.data:
            if re.search(keyword, index["prompt"], re.IGNORECASE):
                query_results.append(index)
        if query_results == []:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "No matches found for '{query}'".format(query=keyword)}

        return query_results


@app.get("/joke/random", status_code=status.HTTP_200_OK, tags=["Get a random joke"])
@limiter.limit("5/minute")
def random_joke(request: Request):
    random_int = random.randrange(1, 47)
    joke = supabase.table("Jokes").select("*").eq("id", random_int).execute()

    return joke


@app.get("/joke/{id}", status_code=status.HTTP_200_OK, tags=["Get joke by id"])
@limiter.limit("5/minute")
def id_joke(request: Request, response: Response, id: int):
    if isinstance(id, int):
        joke = supabase.table("Jokes").select("*").eq("id", id).execute()
        if joke.data == []:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "No joke found with id {id}".format(id=id)}
            
    return joke
