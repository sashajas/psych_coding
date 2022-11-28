from psychopy import visual, monitors, event, core

#define monitor
lMon = monitors.Monitor('lMon', width=31.00, distance = 60) #setup variable mon1 for my laptop monitor with measured width & distance
lMon.setSizePix([1920,1080]) #set pix based on laptop display 

#define window
win=visual.Window(monitor=lMon,color='white',fullscr=True) 

text = visual.TextStim(win,color='black') 
fix = visual.TextStim(win, text='+',color='black')

for trial in range(2): 
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    event.clearEvents() 
    
    text.text = 'Make keypress for trial '+str(trial+1)
    text.draw()
    win.flip() 
    core.wait(2)
    
    keys = event.getKeys(keyList=['1','2','3','4'])
    print('Keys pressed:',keys)
    if keys: 
        firstResp = keys[0]
    print('Keys pressed:',keys)
    print('Main response:',firstResp) 
    
win.close() 
    

    