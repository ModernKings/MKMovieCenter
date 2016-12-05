#!/usr/bin/python
#coding: utf-8
import urllib2
import time
from time import gmtime, strftime

nowPlayingUrl = 'https://movie.douban.com/nowplaying/beijing/'
scheduleTime = 14
def RequestNowPlayingList(url):
        while True :
                currentTime = strftime("%Y%m%d_%H:%M:%S", time.localtime(time.time()))
                print currentTime
                filename = './raw_nowplaying_pages/' + currentTime + '.html'
                fp = open(filename,'w')

                #url = 'https://api.douban.com/v2/movie/'+ filename #+ '?apikey={apikey}'
                print url
                
                req = urllib2.Request(url)
                res = urllib2.urlopen(req)
                html = res.read()
                fp.write(html)     
                res.close
                time.sleep(5)
                fp.close()

if __name__ == "__main__" :
        RequestNowPlayingList(nowPlayingUrl)