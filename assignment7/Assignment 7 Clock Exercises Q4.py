##############################
#CLOCK EXERCISES Q4
##############################
from psychopy import visual, monitors, event, core
import os 
import numpy as np

#define monitor
lMon = monitors.Monitor('lMon', width=31.00, distance = 60) #setup variable mon1 for my laptop monitor with measured width & distance
lMon.setSizePix([1920,1080]) #set pix based on laptop display 
#define window
win=visual.Window(monitor=lMon,color='white',fullscr=True) #window is defined 

#define directories
mainDir = os.getcwd()
imageDir = os.path.join(mainDir,'images')

#define start,block,end text & variables
startMsg = 'Experiment beginning now.'
blockMsg = 'Beginning Block '
endMsg = 'End of trial ' 
nBlocks = 2
nTrials = 3
cText = visual.TextStim(win,color='black') #initialize current text as window 

#define stimuli 
stims = []
for i in range(10):
    n=str(i+1)
    if i <=8: #single digit
        stims.append('face'+'0'+n+'.jpg')
    else:
        stims.append('face'+n+'.jpg')
np.random.shuffle(stims)  #shuffle the list of images

fixCross = visual.TextStim(win, text='+',color='black') #initialize fixation cross as textStim
currentImg = visual.ImageStim(win) #set current image as imageStim


##################
#START EXPERIMENT
##################

trialTimer = core.Clock() #clock is defined before trial
blockTimer = core.Clock()
waitTimer = core.Clock()

cText.text = startMsg #set current text to start message
waitTimer.reset()
while waitTimer.getTime() <=2:
    cText.draw()  #display text
    win.flip()

#################
#BLOCK SEQUENCE
#################
for block in range(nBlocks): #iterate over number of blocks (in this case, 2) 
    blockTimer.reset()
    
    cText.text = blockMsg + str(block+1) #set current text to the block message 
    waitTimer.reset()
    while waitTimer.getTime() <=2:
        cText.draw()  #display text
        win.flip()

    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials):
        #=====================
        #START TRIAL
        #===================== 
        trialTimer.reset()
        
        waitTimer.reset()
        while waitTimer.getTime() <=2:
            fixCross.draw() #display fixation cross
            win.flip()
        
        currentImg.image = os.path.join(imageDir, stims[trial]) #pull image from image directory, set as current image
        waitTimer.reset()
        while waitTimer.getTime() <=2:
            currentImg.draw() #display image
            win.flip()
        
        cText.text = endMsg + str(trial+1) #set current text to end trial message
        waitTimer.reset()
        while waitTimer.getTime() <=2:
            cText.draw() #display text 
            win.flip()
        
        print('Trial', trial+1,'timer:',trialTimer.getTime())
        
    print('Block', block+1,'timer:',blockTimer.getTime())
#======================
# END OF EXPERIMENT
#======================        
closeText = visual.TextStim(win,text='Thank you for participating. This experiment is now over.',color='black') #closing text once experiment is complete 
waitTimer.reset()
while waitTimer.getTime() <=2:
    closeText.draw() #display text 
    win.flip()

win.close() #close experiment