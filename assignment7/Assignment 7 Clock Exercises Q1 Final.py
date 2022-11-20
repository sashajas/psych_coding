####################
#CLOCK EXERCISES Q1
####################

#initalize all necessary elements for trial loop 
#########################################################################################

from psychopy import visual, monitors, event, core
import numpy as np 

#define monitor/win 
lMon = monitors.Monitor('lMon', width=31.00, distance = 60) #setup variable mon1 for my laptop monitor with measured width & distance
lMon.setSizePix([1920,1080])                                #set pix based on laptop display 

win=visual.Window(monitor=lMon,color='white',fullscr=True) #window is defined 

#define os
import os 
mainDir = os.getcwd() #set main directory
imageDir = os.path.join(mainDir,'images') #set image directory

#define stimuli 
fixCross = visual.TextStim(win, text='+',color='#000000') #fixation cross is initalized

endText = visual.TextStim(win, text='End of trial', color='black') #initialize current text as window 

stims = []
for i in range(10):
    n=str(i+1)
    if i <=8: #single digit
        stims.append('face'+'0'+n+'.jpg')
    else:
        stims.append('face'+n+'.jpg')
currentImg = visual.ImageStim(win) #set current image as imageStim
np.random.shuffle(stims)  #shuffle the list of images

#########################################################################
#Q1 
waitTimer = core.Clock() #clock is defined before trial

for trial in range(2):
 
    fixCross.draw() #display fixation cross
    win.flip()
    waitTimer.reset()
    core.wait(2)  #Lv 4 Tutorial contents dictates to make experiment run with waitKeys() until Lv 5 is completed 
    print('Fixation cross time:',waitTimer.getTime())  #waitTimer duration prints 
        
    currentImg.image = os.path.join(imageDir, stims[trial]) #pull image from image directory, set as current image
    currentImg.draw() #display image
    win.flip()
    waitTimer.reset()
    core.wait(2)
    print('Image time:',waitTimer.getTime())  #waitTimer duration prints 
    
    endText.draw() #display text 
    win.flip()
    waitTimer.reset()
    core.wait(2)
    print('End text time:',waitTimer.getTime())  #waitTimer duration prints 
win.close()
