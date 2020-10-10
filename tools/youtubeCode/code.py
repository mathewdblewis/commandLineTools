#!/usr/local/bin/python3

from os import system; from time import sleep
import urllib.request; from sys import argv
from multiprocessing import Pool
import argparse; import pathlib
from json import loads,dumps



def titleAndVids(url):
	# returns (title,vids) where vids is a list of all the vids
	# currently listed on the channels video page
	# and where title is the title of the channel
	# each vid is a tuple (vidTitle,url)
	# where vidTitle is the title of the video and url is the url of the video
	try:
		html = urllib.request.urlopen(url).read().decode()
		title = html.split('<meta name="title" content="')[1].split('">')[0]
		title = "'".join(title.split('&#39;'))
		
		L = [x.split('"url":"')[:2] for x in html.split('"title":{"runs":[{"text":"')[1:]]
		vids = []
		for l in L:
			vidTitle = '"'.join(l[0].split('"}],')[0].split('\\"'))
			end = 'Want to subscribe to this channel?'
			if vidTitle[:len(end)] == end: break
			vidUrl = l[1].split('","')[0]
			vids += [(vidTitle,'https://youtube.com'+vidUrl)]
		return (title,vids)
	except: return ('','')

def allVids(urls):
	# return a dictionary with keys as channel title and values as lists
	# of videos on the channels video page
	return {x[0]:x[1] for x in Pool().map(titleAndVids,urls)}

def channelUrls(channelFile):
	# returns a list of all channel urls given in the input file
	return [x for x in open(channelFile,'r').read().split('\n') if x!='']

def openUrls(urls,browser):
	if browser == '':
		[print(url) for url in urls]
		return
	if urls == []: return
	system("open '" + urls[0] + "' -a " + browser)
	sleep(1)
	[system("open '" + v + "' -a " + browser) for v in urls[1:]]

def titleToUrl(title):
	try:
		title = ''.join('+'.join(title.split(' ')).split("'"))
		url   = 'https://www.youtube.com/results?search_query=' + title
		html  = urllib.request.urlopen(url).read().decode()
		url   = 'https://www.youtube.com/channel/'
		return url+html.split('channelId":"')[1].split('"')[0]
	except: return ''




def unwatched(channelFile,browser,maxnew):
	# takes a channel file (list of channel urls)
	# maxnew (maximum number of new videos to open)
	# browser (the name of the browser to open the videos in)
	# if browser is an empty string, the video urls are printed to STDOUT
	watched,watchedFile = [],channelFile.split('.txt')[0]+'.json'
	try: watched = loads(open(watchedFile,'r').read())
	except: pass
	vids = allVids(channelUrls(channelFile))
	vids = [a for b in [[x[1] for x in vids[channel]] for channel in vids] for a in b]
	newVids = [x for x in vids if x not in watched][:maxnew]
	open(watchedFile,'w').write(dumps(watched+newVids))
	openUrls(newVids,browser)

def latestVids(channelFile,browser):
	vids = allVids(channelUrls(channelFile))
	vids = [vids[channel][0][1] for channel in vids]
	openUrls(vids,browser)

def main():
	return
	parser = argparse.ArgumentParser()
	parser.add_argument('channels',type=str,nargs='?',help='')
	parser.add_argument('browser',type=str,nargs='?',help='')
	parser.add_argument('maxnew',type=int,nargs='?',help='')
	parser.add_argument('func',type=str,nargs='?',help='')
	args = parser.parse_args()

	channels = 'channels.txt'
	browser = 'Firefox'
	maxnew = -1
	func = 'unwatched'
	# if args.channels != None: channels = args.channels.split('=')[1]
	print(args)
	if args.browser != None: browser = args.browser.split('=')[1]
	if args.maxnew != None: maxnew = args.maxnew.split('=')[1]
	if args.func != None: func = args.func.split('=')[1]

	print(channels,browser,maxnew,func)









if __name__ == '__main__':
	path = str(pathlib.Path(__file__).parent.absolute())+'/'
	channels = path+'channels.txt'

	unwatched(channels,'Firefox',10)
	# latestVids(channels,'Firefox')














