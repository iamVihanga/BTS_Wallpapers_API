from requests_html import HTMLSession

class Scraper():
    def __init__(self):
        self.baseURL = 'https://wallpapercave.com

        # Session
        self.s = HTMLSession()

    def getCategories(self):
        url = 'https://wallpapercave.com/search?q=BTS'
        res = self.s.get(url)
        categoryList = []

        categories = res.html.find('a.albumthumbnail')

        for elem in categories:
            item = {
<<<<<<< HEAD
                'categoryName': elem.find('p.title', first=True).text.strip(),
=======
                'categoryName': elem.find('p.title', first=True).text.strip()
>>>>>>> 42a55324a306ae49fd6831fe7b1a1f57e399e143
                'categorySlug': elem.xpath('//a/@href')
            }
            categoryList.append(item)

        return categoryList

    def getWallpapers(self, slug):
        url = self.baseURL + slug
        return url
