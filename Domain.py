from urllib.parse import urlparse

#This class takes the url and removes unnecessary symbols/text
def getDomainName(url):
    try:
        results = getSubDomain(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

def getSubDomain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
