#!/usr/bin/python
#coding: utf-8
import requests
import re
if __name__=="__main__":
	page = requests.get('https://movie.douban.com/nowplaying/beijing/')
	content=page.text.encode("utf-8")
	pattern=re.compile(r'(?<=id=")\d+(?="\n)')
	result=pattern.findall(content)
	for iterm in result:
		print iterm




