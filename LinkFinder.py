from html.parser import HTMLParser
from urllib import parse

#This class parses the html and adds the right links to be crawled and ignores the rest

class LinkFinder(HTMLParser):
    def __init__(self, baseUrl, pageUrl):
        super().__init__()
        self.base_url = baseUrl
        self.page_url = pageUrl
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def pageLinks(self):
        return self.links

    def error(self, message):
        pass

