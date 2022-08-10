import os
from typing import Optional
from fastapi import FastAPI
from supabase import create_client, Client
from dotenv import load_dotenv
from pydantic import BaseModel, Json

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
def all_jokes():
    jokes = supabase.table('Jokes').select('prompt').execute()
    return jokes

@app.get("/joke/search", status_code=200) 
def search_jokes(keyword: Optional[str] = None):
        jokes = supabase.table('Jokes').select('*').eq('prompt', keyword).execute()
        return jokes

@app.get("/joke/{id}", status_code=200) #done
def id_joke(id: int):
    jokes = supabase.table('Jokes').select('*').eq('id', id).execute()
    return jokes

@app.get("/joke/random", status_code=200)
def random_joke():
    jokes = supabase.table('Jokes').select('*').execute()
    return jokes
