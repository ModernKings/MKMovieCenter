#!/usr/bin/python
#coding: utf-8
from os import listdir
from datetime import datetime
import requests
import urllib2
import json

class RequestNowPlayingMovieInfo(object):
	movieListDir = "./nowplaying_id/"
	movieInfoDir = "./nowplaying_info/"
	latestMovieListFIleDate = datetime.strptime('20000101_00:00:00', '%Y%m%d_%H:%M:%S')
	latestMovieListFIle = ""
	url = 'https://api.douban.com/v2/movie/'
	def __init__(self):
		#super(GetNowPlayingMovieInfo, self).__init__()
		pass

	def  loadLatestMovieList(self):
		for f in listdir(self.movieListDir):
			datetime_object = datetime.strptime(f, '%Y%m%d_%H:%M:%S.id')
			if datetime_object > self.latestMovieListFIleDate :
				self.latestMovieListFIleDate = datetime_object
				self.latestMovieListFIle = f
		return self.movieListDir + self.latestMovieListFIle

	def requestMovieInfo(self, id='0'):
		url = self.url + id
		print url

		req = urllib2.Request(url)
		res = urllib2.urlopen(req)

		data = json.load(res)
		return data
	def  saveMovieInfo(self, id="0", info="info"):
		fp = open(self.movieInfoDir+id.strip()+'.info', 'w')
		fp.write(str(info))
		fp.close()
		pass

if __name__ == '__main__':
	requestNowPlayingMovieInfo = RequestNowPlayingMovieInfo()
	latestMoiveFile = requestNowPlayingMovieInfo.loadLatestMovieList()
	print latestMoiveFile
	fp = open(latestMoiveFile, 'r')
	for movieId in fp :
		info = requestNowPlayingMovieInfo.requestMovieInfo(movieId)
		requestNowPlayingMovieInfo.saveMovieInfo(movieId, info)
	fp.close()
