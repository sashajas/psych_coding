##############################
# STIMULUS EXERCISES
##############################
from psychopy import visual, monitors, event
import os 
import numpy as np

#define monitor
lMon = monitors.Monitor('lMon', width=31.00, distance = 60) #setup variable mon1 for my laptop monitor with measured width & distance
lMon.setSizePix([1920,1080]) #set pix based on laptop display 
#define window
win=visual.Window(monitor=lMon,color=[0.78,0.63,0.78],fullscr=True) #window is defined 

#define directories
mainDir = os.getcwd()
imageDir = os.path.join(mainDir,'images')

#define start,block,end text & variables
startMsg = 'Experiment beginning now.'
blockMsg = 'Press any key to continue to the next block.'
endMsg = 'End of trial ' 
nBlocks = 2
nTrials = 3
cText = visual.TextStim(win) #initialize current text as window 

#define stimuli 
stims = ['face01.jpg','face02.jpg','face03.jpg'] #list of stimuli from images
fixCross = visual.TextStim(win, text='+',color=[0,0,0],bold=True) #initialize fixation cross as textStim
currentImg = visual.ImageStim(win) #set current image as imageStim
np.random.shuffle(stims)  #shuffle the list of images

##################
#START EXPERIMENT
##################
cText.text = startMsg #set current text to start message
cText.draw()  #display text
win.flip()
event.waitKeys() 

##################
#BLOCK SEQUENCE
##################
for block in range(nBlocks): #iterate over number of blocks (in this case, 2) 
    cText.text = blockMsg #set current text to the block message 
    cText.draw()  #display text
    win.flip()
    event.waitKeys() 
    #trials do not need to be randomized here as stimuli were put in random order above already
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials):
        #=====================
        #START TRIAL
        #===================== 
        #stimuli properties are being left as default - no changes needed in this circumstance 
        fixCross.draw() #display fixation cross
        win.flip()
        event.waitKeys() #Lv 4 Tutorial contents dictates to make experiment run with waitKeys() until Lv 5 is completed 
        
        currentImg.image = os.path.join(imageDir, stims[trial]) #pull image from image directory, set as current image
        currentImg.draw() #display image
        win.flip()
        event.waitKeys() #Lv 4 Tutorial contents dictates to make experiment run with waitKeys() until Lv 5 is completed 
        
        cText.text = endMsg + str(trial+1) #set current text to end trial message
        cText.draw() #display text 
        win.flip()
        event.waitKeys()#Lv 4 Tutorial contents dictates to make experiment run with waitKeys() until Lv 5 is completed 

#======================
# END OF EXPERIMENT
#======================        
closeText = visual.TextStim(win,text='Thank you for participating. This experiment is now over.') #closing text once experiment is complete 
closeText.draw() #display text 
win.flip()
event.waitKeys()
win.close() #close experiment