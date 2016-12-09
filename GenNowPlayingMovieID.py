#!/usr/bin/python
#coding: utf-8
import requests
import re
import time
from time import gmtime, strftime

class GenNowPlayingID(object):
	"""docstring for ClassName"""
	def __init__(self):
		#super(ClassName, self).__init__()
		# self.arg = arg
		pass

	def GenNowPlayingIdList(self):
		page = requests.get('https://movie.douban.com/nowplaying/beijing/')
		content=page.text.encode("utf-8")
		pattern=re.compile(r'(?<=id=")\d+(?="\n)')
		result=pattern.findall(content)

		currentTime = strftime("%Y%m%d_%H:%M:%S", time.localtime(time.time()))
		print currentTime
		filename = './nowplaying_id/' + currentTime + '.id'
		fp = open(filename,'w')

		for iterm in result:
			fp.write(iterm+"\n")
		fp.close()

if __name__=="__main__":
	genNowPlayingID = GenNowPlayingID()
	genNowPlayingID.GenNowPlayingIdList()


