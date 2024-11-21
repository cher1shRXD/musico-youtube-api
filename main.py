from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.query_model import QueryModel
from services.search_youtube import search_youtube

app = FastAPI()

origins = [
  "http://localhost:3000",
  "https://musico.cher1shrxd.me",
  "http://localhost:5173"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.post("/")
async def yt_search(query: QueryModel):
  return search_youtube(query.query)