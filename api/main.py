import os
import random
import re
from typing import Optional
from fastapi import FastAPI, Request
from supabase import create_client, Client
from dotenv import load_dotenv
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

load_dotenv()
app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

url = os.getenv('SUPABASE_SUPAFAST_URL')
key = os.getenv('SUPABASE_SUPAFAST_KEY')
supabase: Client = create_client(url, key)

@app.get("/")
def index():
    return {
        "message": "Please refer to the documentation for more or visit http://localhost:8000/docs"
    }

@app.get("/jokes", status_code=200)
@limiter.limit("5/minute")
def all_jokes(request: Request, max_results: Optional[int] = 47):
    jokes = supabase.table('Jokes').select('*').limit(max_results).execute()

    return jokes

@app.get("/joke/search", status_code=200)
@limiter.limit("5/minute")
def search_jokes(request: Request, keyword: Optional[str] = None):
    if keyword is None:
        return supabase.table('Jokes').select('*').execute()
    else:
        query_results = []
        jokes = supabase.table('Jokes').select('*').execute()

        for index in jokes.data:
                if re.search(keyword, index['prompt'], re.IGNORECASE):
                        query_results.append(index)
        if query_results == []:
                return {
                    "message": "No matches found for '{query}'".format(query=keyword)
                }
        return query_results

@app.get("/joke/random", status_code=200)
@limiter.limit("5/minute")
def random_joke(request: Request):
    random_int = random.randrange(1, 47)
    joke = supabase.table('Jokes').select('*').eq('id', random_int).execute()

    return joke

@app.get("/joke/{id}", status_code=200)
@limiter.limit("5/minute")
def id_joke(request: Request, id: int):
    joke = supabase.table('Jokes').select('*').eq('id', id).execute()

    return joke

