from requests_html import HTMLSession

class Scraper():
    def __init__(self):
        self.url = 'https://wallpapercave.com/categories/anime'
        self.baseURL = 'https://wallpapercave.com/'

        # Session
        self.s = HTMLSession()

    def scrapeData(self):
        r = self.s.get(self.url)

        print(r.status_code)