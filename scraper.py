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
                'categoryName': elem.find('p.title', first=True).text.strip()
                'categorySlug': elem.xpath('//a/@href')
            }
            categoryList.append(item)

        return categoryList
