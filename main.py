from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()
scraper = Scraper()

@app.get('/')
async def getRoot():
    return 'Welcome to BTS Wallpaper World..!!!'


@app.get('/categories')
async def getCategories():
    return scraper.getCategories()

