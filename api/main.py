import os
import random
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
def all_jokes(max_results: Optional[int] = 10):
    jokes = supabase.table('Jokes').select('*').limit(max_results).execute()

    return jokes

@app.get("/joke/search", status_code=200) 
def search_jokes(keyword: Optional[str] = None):
        jokes = supabase.table('Jokes').select('*').execute()
        for index, row in jokes:
            if keyword in row[0]:
                return row

@app.get("/joke/random", status_code=200) #done
def random_joke():
    random_int = random.randrange(1, 47)
    jokes = supabase.table('Jokes').select('*').eq('id', random_int).execute()

    return jokes

@app.get("/joke/{id}", status_code=200) #done
def id_joke(id: int):
    jokes = supabase.table('Jokes').select('*').eq('id', id).execute()

    return jokes

