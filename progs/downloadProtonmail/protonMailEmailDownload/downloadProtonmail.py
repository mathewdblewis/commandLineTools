# Mathew Lewis, May 2020
# This program downloads emails from protonmail
# run the code, then switch tabs to protonmail open in firefox

from pyautogui import locate,scroll,click,screenshot,press,moveTo
from time import sleep
import numpy as np; from PIL import Image; from scipy import signal
from subprocess import run, check_output as call

def date(l):
	return l[-29:16-29].replace('T','.').replace('-','.').replace(' ','.')

def mvMailToDir():
	L = call("ls *.eml" + dir, shell=True).decode().split("\n")[:-1]
	for l in L:
		old = '\\ '.join(l.split(' '))
		new =   '_'.join(l.split(' '))
		temp = "mv ~/Downloads/" + old + " emails/" + date(l) + '_' + new
		call(temp,shell=True)

def clickOn(imgFile,x,y,w,h):
	B = None
	small = Image.open(imgFile)
	while B == None: B = locate(small,screenshot(region=(x,y,w,h)))
	click(x/2+B.left/2+B.width/4,y/2+B.top/2+B.height/4)


while True:
	clickOn("buttons/more.png",1200*2,250*2,220*2,650*2)
	scroll(-19); sleep(.2); moveTo(500,500)
	clickOn("buttons/expo.png",1230*2,250*2, 30*2,650*2)
	clickOn("buttons/ok.png",   800*2,560*2,100*2, 40*2)
	press('escape'); press('down'); press('enter')
	mvMailToDir()










