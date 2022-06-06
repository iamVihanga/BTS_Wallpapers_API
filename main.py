from fastapi import FastAPI
from scraper import Scraper
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
scraper = Scraper()

# Handelling CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def getRoot():
    return 'Welcome to BTS Wallpaper World..!!!'


@app.get('/categories')
async def getCategories():
    return scraper.getCategories()


@app.get('/categories/{slug}')
async def getWallpapers(slug):
    return scraper.getWallpapers(slug)
