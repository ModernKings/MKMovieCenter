#!/usr/bin/python
#coding: utf-8
import requests
import time
from time import gmtime, strftime
import urllib2
import json
from pprint import pprint

# nowPlayingUrl = 'http://127.0.0.1:8000/snippets'
nowPlayingUrl = 'https://api.douban.com/v2/movie/subject/26683290'

def RequestNowPlayingList(url):
                #url = 'https://api.douban.com/v2/movie/'+ filename #+ '?apikey={apikey}'
                print url
                html = requests.get(url)
                print html
                
                print 'urllib2'
                req = urllib2.Request(url)
                res = urllib2.urlopen(req)
                # html2 = res.read().encode('gbk')
                # print html2

                data = json.load(res)
                print data['rating']

if __name__ == "__main__" :
        RequestNowPlayingList(nowPlayingUrl)