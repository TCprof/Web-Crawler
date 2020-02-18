from urllib.request import urlopen
from LinkFinder import LinkFinder
from main import *
from Domain import *

#holds the functions needed for a spider to crawl a webpage and links the necessary files
class Spider:

    projectName = ''
    baseUrl = ''
    domainName = ''
    queueFile = ''
    crawledFile = ''
    queue = set()
    crawled = set()
    #assigns the correct varaible names to the right variables
    def __init__(self, projectName, baseUrl, domainName):
        Spider.projectName = projectName
        Spider.baseUrl = baseUrl
        Spider.domainName = domainName
        Spider.queueFile = Spider.projectName + '/queue.txt'
        Spider.crawledFile = Spider.projectName + '/visited.txt'
        self.boot()
        self.crawlPage('First spider', Spider.baseUrl)

    @staticmethod
    def boot():
        create_project_dir(Spider.projectName)
        create_data_files(Spider.projectName, Spider.baseUrl)
        Spider.queue = fileToSet(Spider.queueFile)
        Spider.crawled = fileToSet(Spider.crawledFile)

    @staticmethod
    #crawls new links and updates the queue and crawled files
    def crawlPage(name, pageUrl):
        if pageUrl not in Spider.crawled:
            print(name + ' now crawling ' + pageUrl)
            print('Queue ' + str(len(Spider.queue)) + '     Crawled ' + str(len(Spider.crawled)))
            Spider.addLinks(Spider.gatherLinks(pageUrl))
            Spider.queue.remove(pageUrl)
            Spider.crawled.add(pageUrl)
            Spider.updateFiles()

    @staticmethod
    #determines whether or not the Url is of the right  type
    def gatherLinks(pageUrl):
        htmlString = ''
        try:
            response = urlopen(pageUrl)
            if 'text/html' in response.getheader('Content-Type'):
                htmlBytes = response.read()
                htmlString = htmlBytes.decode('utf-8')
            finder = LinkFinder(Spider.baseUrl, pageUrl)
            finder.feed(htmlString)
        except Exception as e:
            print(str(e))
            return set()
        return finder.pageLinks()

    @staticmethod
    def addLinks(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domainName not in url:
                continue
            Spider.queue.add(url)


    @staticmethod
    def updateFiles():
        setToFile(Spider.queue, Spider.queueFile)
        setToFile(Spider.crawled, Spider.crawledFile)


