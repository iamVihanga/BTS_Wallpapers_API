from requests_html import HTMLSession

class Scraper():
    def __init__(self):
        self.baseURL = 'https://wallpapercave.com/'

        # Session
        self.s = HTMLSession()

    def getCategories(self):
        url = 'https://wallpapercave.com/search?q=BTS'
        res = self.s.get(url)
        categoryList = []

        categories = res.html.find('a.albumthumbnail')

        for elem in categories:
            item = {
                'categoryName': elem.find('p.title', first=True).text.strip(),
                'categoryThumbnail': elem.find('img.thumbnail', first=True).attrs['src'],
                'wallpapersCount': elem.find('span.overlay', first=True).text.strip(),
                'categorySlug': elem.xpath('//a/@href')[0][1:]
            }
            categoryList.append(item)

        return categoryList

    def getWallpapers(self, slug):
        url = self.baseURL + slug
        res = self.s.get(url)

        wallpapersList = []

        wallpapers = res.html.find('img.wimg')

        for elem in wallpapers:
            wall = self.baseURL + elem.attrs["src"][1:]
            wallpapersList.append(wall)

        return wallpapersList


