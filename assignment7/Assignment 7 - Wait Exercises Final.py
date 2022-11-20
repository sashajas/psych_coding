from psychopy import visual, monitors, event

lMon = monitors.Monitor('lMon', width=31.00, distance = 60) #setup variable mon1 for my laptop monitor with measured width & distance
lMon.setSizePix([1920,1080])                                #set pix based on laptop display 

win=visual.Window(monitor=lMon,color='white',fullscr=True) #window is defined 

import os 
mainDir = os.getcwd() #set main directory
imageDir = os.path.join(mainDir,'images') #set image directory

######################
#WAIT EXERCISES
######################

from psychopy import core
fixCross = visual.TextStim(win, text='+',color='#000000')
image=visual.ImageStim(win)
#=====================
#START TRIAL
#===================== 
fixCross.draw()
win.flip()
core.wait(2)
        
image.image = os.path.join(imageDir,'face01.jpg')
image.draw()
win.flip()
core.wait(0.5)
        
text=visual.TextStim(win,text='End of trial',color='black')
text.draw()
win.flip()
core.wait(1)
