from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()
walls = Scraper()

@app.get('/')
async def getRes():
    return walls.scrapeData()