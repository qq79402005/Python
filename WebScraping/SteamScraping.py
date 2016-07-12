from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import socket
import urllib
import re

# global url lists
steam_main_urls = []
steam_tag_urls = []
steam_app_urls = []

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
        bsObj = BeautifulSoup(html, 'html.parser')
    except AttributeError as e:
        html.close()
        return None

    html.close()
    return bsObj

# get all links
def getAllLinks(url, pattern, olist):
    bsObj = getBSObj(url)
    if bsObj != None :
        for link in bsObj.findAll('a'):
            if 'href' in link.attrs :
                href = link.attrs['href']
                if pattern.match(href):
                    if olist.count(href)==0 :
                        olist.append(href)

    return

# read html and analyse
if __name__ == '__main__':
    # get all tags
    #idx = 0
    #getAllLinks('http://store.steampowered.com/', re.compile('http://store.steampowered.com/tag/en/.*'), steam_tag_urls)
    #while idx < len(steam_tag_urls) :
    #    print('processing get tags...[%d/%d]%s' % (idx, len(steam_tag_urls), steam_tag_urls[idx]))
    #    getAllLinks(steam_tag_urls[idx], re.compile('http://store.steampowered.com/tag/en/.*'), steam_tag_urls)
    #    idx = idx + 1

    # get all apps
    #idx = 0
    #while idx < len(steam_tag_urls) :
    #    print('processing get apps...[%d/%d]%s' % (idx, len(steam_tag_urls), steam_tag_urls[idx]))
    #    getAllLinks( steam_tag_urls[idx], re.compile('http://store.steampowered.com/app/[0-9]/'), steam_app_urls)
    #    idx = idx + 1

    # print all steam apps
    getAllLinks( 'http://store.steampowered.com/tag/en/RPG/?snr=1_237_237__12', re.compile('http://store.steampowered.com/app/.*'), steam_app_urls)
    for url in steam_app_urls:
        print( url)