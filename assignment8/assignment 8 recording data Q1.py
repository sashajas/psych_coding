from psychopy import core, event, visual, monitors
import numpy as np

#define monitor
lMon = monitors.Monitor('lMon', width=31.00, distance = 60) #setup variable mon1 for my laptop monitor with measured width & distance
lMon.setSizePix([1920,1080]) #set pix based on laptop display 

#define window
win=visual.Window(monitor=lMon,color='white',fullscr=True) 

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=1
myText=visual.TextStim(win,color='black')
rtClock = core.Clock()  # create a response time clock
cdTimer = core.CountdownTimer() #add countdown timer

#create dict 
expDict = {} 
#create lists for problems
prob = [[0]*nTrials]*nBlocks
corrResp = [[0]*nTrials]*nBlocks

#create problems and solutions to show
mathProblems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
probSol = list(zip(mathProblems,solutions))

for block in range(nBlocks):
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = probSol[np.random.choice(4)]
        corrResp[block][trial] = prob[block][trial][1]
        
        rtClock.reset()  # reset timing for every trial
        cdTimer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cdTimer.getTime() > 0: #for 3 seconds

            myText.text = prob[block][trial][0] #present the problem for that trial
            myText.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    expDict['Trial '+str(trial+1)+' '+'reaction time'] = rtClock.getTime()
                    #get key for only the first response in that loop
                    expDict['Trial '+str(trial+1)+' '+'key'] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if expDict['Trial '+str(trial+1)+' '+'key'] == str(corrResp[block][trial]):
            expDict['Trial '+str(trial+1)+' '+'subject accuracy'] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif expDict['Trial '+str(trial+1)+' '+'key'] != str(corrResp[block][trial]):
            expDict['Trial '+str(trial+1)+' '+'subject accuracy'] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corrResp[block][trial], 'subject response=',expDict['Trial '+str(trial+1)+' '+'key'], 
              'subject accuracy=',expDict['Trial '+str(trial+1)+' '+'subject accuracy'])

win.close()