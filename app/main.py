import os
import asyncio
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
from app.meme import generateMemeImgs

app = FastAPI()

# allow origin
origins = os.getenv('CORS_ALLOW_ORIGIN').split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# get meme images
loop = asyncio.get_event_loop()  # create event loop
loop.create_task(generateMemeImgs(-1))


@app.get("/")
def read_root():
    return {"app-name": os.getenv("APP_NAME")}


@app.get("/memes", response_class=JSONResponse)
async def read_memes():
    f = open('meme-imgs_-1.json')
    data = json.load(f)
    return data


@app.get("/meme/{page_limit}", response_class=JSONResponse)
async def read_meme(page_limit):
    await generateMemeImgs(int(page_limit))
    f = open('meme-imgs_'+page_limit+'.json')
    data = json.load(f)
    return data
