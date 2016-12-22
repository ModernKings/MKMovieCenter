#!/usr/bin/python
#coding: utf-8
import urllib2
import time
from time import gmtime, strftime
import logging
from logging.config import fileConfig

class RequestNowPlayingRaw(object):
        """docstring for ClassName"""
        nowPlayingUrl = 'https://movie.douban.com/nowplaying/beijing/'
        scheduleTime = 14
        fileConfig('logging.properties')

        def __init__(self):
                pass
                
        def RequestNowPlayingRawData(self):
                url = self.nowPlayingUrl

                while True :
                        currentTime = strftime("%Y%m%d_%H:%M:%S", time.localtime(time.time()))
                        print currentTime
                        filename = './raw_nowplaying_pages/' + currentTime + '.html'
                        fp = open(filename,'w')

                        #url = 'https://api.douban.com/v2/movie/'+ filename #+ '?apikey={apikey}'
                        logging.info("Request raw data from %s", url)
                        
                        req = urllib2.Request(url)
                        res = urllib2.urlopen(req)
                        html = res.read()
                        fp.write(html)
                        res.close
                        time.sleep(5)
                        fp.close()

if __name__ == "__main__" :
        requestNowPlayingRaw = RequestNowPlayingRaw()
        while True:
                requestNowPlayingRaw.RequestNowPlayingRawData()
                pass
