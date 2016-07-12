from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import socket
import urllib

# get title by url
def getBSObj(url):
    try:
 #       proxy_support = urllib.request.ProxyHandler({'http':'http://213.136.77.246:80'})
 #       opener = urllib.request.build_opener( proxy_support)
 #       urllib.request.install_opener(opener)
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html)
    except AttributeError as e:
        html.close()
        return None

    html.close()
    return bsObj

# get all links
def getAllLinks(url):
    bsObj = getBSObj(url)
    if bsObj != None :
        for link in bsObj.findAll('a'):
            if 'href' in link.attrs :
                print(link.attrs['href'])

# read html and analyse
if __name__ == '__main__':
    socket.setdefaulttimeout( 30)
    getAllLinks('http://store.steampowered.com/');

