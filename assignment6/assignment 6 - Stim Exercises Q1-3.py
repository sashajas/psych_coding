from psychopy import visual, monitors, event

lMon = monitors.Monitor('lMon', width=31.00, distance = 60) #setup variable mon1 for my laptop monitor with measured width & distance
lMon.setSizePix([1920,1080])                                #set pix based on laptop display 

win=visual.Window(monitor=lMon,color=[1,1,1],fullscr=True) #window is defined 

import os 
mainDir = os.getcwd() #set main directory
imageDir = os.path.join(mainDir,'images') #set image directory

import random

##Q1. 
totalImg = ['face01.jpg','face02.jpg','face03.jpg','face04.jpg','face05.jpg','face06.jpg','face07.jpg','face08.jpg','face09.jpg','face10.jpg']
#list of all images in images file
cImg = random.choice(totalImg) #select random choice as current image (cImg) 

myImage = visual.ImageStim(win,size = (400,400),units='pix') #initializes image in window with size set to 400x400 px 
#this results in images that have been stretched or squished to fit the fixed size requested
#this can be rectified by not using a fixed size, but by using 'height' as units
#I cannot determine a way to resize an image while keeping it scaled 

myImage.image=os.path.join(imageDir,cImg) #initialize window to show current image
myImage.draw() #draw, flip, etc. 
win.flip()
event.waitKeys() 

##Q2. 

quad1Image = visual.ImageStim(win,image=os.path.join(imageDir,cImg),pos=(0.5,0.5)) #initalize cImg in each quadrant using pos componenet
quad2Image = visual.ImageStim(win,image=os.path.join(imageDir,cImg),pos=(-0.5,0.5))
quad3Image = visual.ImageStim(win,image=os.path.join(imageDir,cImg),pos=(0.5,-0.5))
quad4Image = visual.ImageStim(win,image=os.path.join(imageDir,cImg),pos=(-0.5,-0.5))
#quadrants can be determined by changing the signs on the values to relocate image 
#eg. ++,+-,-+,-- results in one image in each quadrant 

quad1Image.draw() #draw each image iteratively
win.flip()
event.waitKeys() 

quad2Image.draw()
win.flip()
event.waitKeys() 

quad4Image.draw()
win.flip()
event.waitKeys() 

quad3Image.draw()
win.flip()
event.waitKeys() 

##Q3.
fixCross = visual.TextStim(win, text='+',color=[0,0,0],bold=True) #set fixation cross as TextStim using text '+', also setting text color and formatting here
fixCross.draw() #show cross in window 
win.flip()
event.waitKeys()
