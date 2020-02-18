import threading
from queue import Queue

from spider import Spider
from Domain import *
from main import *

#This is the main running class, uses up to 8 concurrent threads
#need to limit the total amount of links

PROJECT_NAME = 'Output'
#HOMEPAGE can be changed, using wikipedia creates a lot of links
HOMEPAGE = 'https://en.wikipedia.org/wiki/Wikipedia:!Short_articles'
DOMAIN_NAME = getDomainName(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/visited.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

#creates the 'spiders' that crawl the links
def createWorkers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.start()


def work():
    while True:
        url = queue.get()
        Spider.crawlPage(threading.current_thread().name, url)
        queue.task_done()


def createJobs():
    for link in fileToSet(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


def crawl():
    queuedLinks = fileToSet(QUEUE_FILE)
    if len(queuedLinks) > 0:
        print(str(len(queuedLinks)) + ' links in the queue')
        createJobs()


createWorkers()
crawl()
