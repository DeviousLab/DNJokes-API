import os
import random
import re
from typing import Optional
from fastapi import FastAPI
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

url = os.getenv('SUPABASE_SUPAFAST_URL')
key = os.getenv('SUPABASE_SUPAFAST_KEY')
supabase: Client = create_client(url, key)

@app.get("/")
def index():
    return {
        "message": "Please refer to the documentation for more or visit http://localhost:8000/docs"
    }

@app.get("/jokes", status_code=200) #done
def all_jokes(max_results: Optional[int] = 47):
    jokes = supabase.table('Jokes').select('*').limit(max_results).execute()

    return jokes

@app.get("/joke/search", status_code=200) 
def search_jokes(keyword: Optional[str] = None):
    if keyword is None:
        return supabase.table('Jokes').select('*').execute()
    else:
        query_results = []
        jokes = supabase.table('Jokes').select('*').execute()

        for index in jokes.data:
                if re.search(keyword, index['prompt'], re.IGNORECASE):
                        query_results.append(index)
                # else:
                #         return {
                #             "message": "No matches found for '{query}'".format(query=keyword)
                #         }
        return query_results

@app.get("/joke/random", status_code=200) #done
def random_joke():
    random_int = random.randrange(1, 47)
    jokes = supabase.table('Jokes').select('*').eq('id', random_int).execute()

    return jokes

@app.get("/joke/{id}", status_code=200) #done
def id_joke(id: int):
    jokes = supabase.table('Jokes').select('*').eq('id', id).execute()

    return jokes

