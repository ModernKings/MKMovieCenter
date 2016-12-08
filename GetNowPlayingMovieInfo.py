#!/usr/bin/python
#coding: utf-8
from os import listdir
from datetime import datetime

class GetNowPlayingMovieInfo(object):
	movieListDir = "./nowplaying_id/"
	latestMovieListFIleDate = datetime.strptime('20000101_00:00:00', '%Y%m%d_%H:%M:%S')
	latestMovieListFIle = ""
	def __init__(self):
		#super(GetNowPlayingMovieInfo, self).__init__()
		pass

	def  readLatestMovieList(self):
		for f in listdir(self.movieListDir):
			datetime_object = datetime.strptime(f, '%Y%m%d_%H:%M:%S.id')
			if datetime_object > self.latestMovieListFIleDate :
				self.latestMovieListFIleDate = datetime_object
				self.latestMovieListFIle = f
		return self.latestMovieListFIle

if __name__ == '__main__':
	getNowPlayingMovieInfo = GetNowPlayingMovieInfo();
	latestMoiveFile = getNowPlayingMovieInfo.readLatestMovieList()
	print latestMoiveFile