##############################
#FRAME BASED TIMING EXERCISES
##############################
from psychopy import visual, monitors, event, core,logging
import os 
import numpy as np

#define monitor
lMon = monitors.Monitor('lMon', width=31.00, distance = 60) #setup variable mon1 for my laptop monitor with measured width & distance
refresh=1.0/60.02
lMon.setSizePix([1920,1080]) #set pix based on laptop display 

#define window
win=visual.Window(monitor=lMon,color='white',fullscr=True) #window is defined 
win.recordFrameIntervals=True #record frame drops 
win.refreshThreshold=1.0/60.0 + 0.004 #4 ms tolerance on monitor refresh rate
logging.console.setLevel(logging.WARNING) #default is ERROR

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
        stims.append('face'+'0'+n+'.jpg') #create file name with 0 before digit 
    else: #double digit or higher
        stims.append('face'+n+'.jpg') #create file name 

np.random.shuffle(stims)  #shuffle the list of images

fixCross = visual.TextStim(win, text='+',color='black') #initialize fixation cross as textStim
currentImg = visual.ImageStim(win) #set current image as imageStim

#set durations
fixDur = 1
imageDur = 2
textDur = 1.5

#set frame counts (whole numbers) 
refresh=1.0/60.0
fixFrames = int(fixDur/refresh)  #fixation frames 
imageFrames = int(imageDur/refresh) #image frames
textFrames = int(textDur/refresh) #text frames 

#total frames
totalFrames = int(fixFrames+imageFrames+textFrames) #sum of all frames

##################
#START EXPERIMENT
##################


cText.text = startMsg #set current text to start message
cText.draw()  #display text
win.flip()
core.wait(2) #2 s wait (core.wait used b/c precise timing is not required for this section) 

#################
#BLOCK SEQUENCE
#################
for block in range(nBlocks): #iterate over number of blocks
    
    cText.text = blockMsg + str(block+1) #set current text to the block message 
    cText.draw()  #display text
    win.flip()
    core.wait(2) #2 s wait (core.wait used b/c precise timing is not required for this section) 
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials):
        #=====================
        #START TRIAL
        #===================== 
        
        for frame in range(totalFrames):
            if 0 <= frame <= fixFrames: #number of frames for fixation alone 
                fixCross.draw() #display fixation cross
                win.flip()
                if frame == fixFrames: #last frame
                    print('End fix frame =',frame) #print the last frame number 
            
            if fixFrames < frame <= (fixFrames+imageFrames): #required number of frames after fixation occurs 
                currentImg.image = os.path.join(imageDir, stims[trial]) #pull image from image directory, set as current image
                currentImg.draw() #display image
                win.flip()
                if frame == (fixFrames+imageFrames): #last image frame 
                    print('End image frame=',frame) 
                    
            if (fixFrames+imageFrames) < frame < totalFrames: 
                cText.text = endMsg + str(trial+1) #set current text to end trial message
                cText.draw() #display text 
                win.flip()
                if frame == (totalFrames-1): #last text frame
                    print('End text frame =',frame) #frame number 
        
        print('Overall, %i frames were dropped.'% win.nDroppedFrames)
#======================
# END OF EXPERIMENT
#======================        
closeText = visual.TextStim(win,text='Thank you for participating. This experiment is now over.',color='black') #closing text once experiment is complete 
closeText.draw() #display text 
win.flip()
core.wait(2) #2 s wait (core.wait used b/c precise timing is not required for this section) 

win.close() #close experiment