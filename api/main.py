import os
from typing import Optional
from fastapi import FastAPI
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

url = os.getenv('SUPABASE_SUPAFAST_URL')
key = os.getenv('SUPABASE_SUPAFAST_KEY')
supabase: Client = create_client(url, key)

@app.get("/jokes", status_code=200)
def jokes():
    jokes = supabase.table('Jokes').select('*').execute()
    return jokes

@app.get("/joke", status_code=200)
def jokes():
    jokes = supabase.table('Jokes').select('*').execute()
    return jokes

@app.get("/joke/random", status_code=200)
def jokes():
    jokes = supabase.table('Jokes').select('*').execute()
    return jokes

@app.get("/joke/{id}", status_code=200)
def jokes():
    jokes = supabase.table('Jokes').select('*').execute()
    return jokes

@app.get("/joke/search", status_code=200)
def search_jokes(keyword: Optional[str] = None, max_results: Optional[int] = 10) -> dict:
    jokes = supabase.table('Jokes').select('*').execute()
    return jokes 
    