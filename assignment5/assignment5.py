#=====================
#IMPORT MODULES
#=====================
import numpy as np
#from psychopy import core, gui, visual, event - completed in PsychoPy coder, did not need to import it 
import json
import csv 
import os
import random 

#=====================
#PATH SETTINGS
#=====================
pics = []
for pic in range(10):
    current = str(pic+1)
    if pic+1 <10:
        pics.append('face0'+current+'.jpg')
    else: 
        pics.append('face'+current+'.jpg')

mainDir = os.getcwd()
imageDir = os.path.join(mainDir,'images')
dataDir = os.path.join(mainDir,'data') 
print(os.path.isdir(imageDir))
print(os.path.isdir(dataDir))
print(os.path.isdir(mainDir))

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
blocks = 2
trials = ['Trial 1','Trial 2','Trial 3','Trial 4','Trial 5','Trial 6','Trial 7','Trial 8',
'Trial 9','Trial 10']
totalTrials = trials*2

numImg = 10

screenHeight = 200
screenWidth = 200 
duration = 1 #second
#all images (fixation cross & image) appear in centre of screen 

startText = 'Focus on the fixation cross.'

#=====================
#PREPARE CONDITION LISTS
#=====================
imgInDir = sorted(os.listdir(imageDir))
if not pics == imgInDir:
    raise Exception('Image lists do not match.') 
counterBal = [] #unclear how this should be done since trial conditions were not laid out - are there multiple groups (control, etc?) 


#=====================
#PREPARE DATA COLLECTION LISTS
#=====================

correctResp = []
allResp = []
accuracyResp = []
times = []
identities = []
properties = []

#=====================
#BLOCK SEQUENCE
#=====================

for block in range(2):
    print('Block number:',block+1,'\n')
    random.shuffle(trials)
    print('Trial order:',trials)
 #=====================
    #TRIAL SEQUENCE
    #=====================    

    for trial in trials:
        print(startText) 
        print(trial)
        
        