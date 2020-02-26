from urllib import request
from factory import CategoryFactory
import analyser
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

class Spider():
    def __init__(self, url, analyser):
        self.url = url
        self.analysers = analyser
    
    def __fetch_cotent(self):
        with request.urlopen(self.url) as r:
            htmls = r.read()
            htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        analyser = CategoryFactory.get_category(self.analysers)
        analyser.analysis(htmls)

    def go(self):
            htmls = self.__fetch_cotent()
            self.__analysis(htmls)
