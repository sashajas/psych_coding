###########################
# DIALOG BOX EXERCISES
###########################

from psychopy import gui
from datetime import datetime
import os

expInfo = {'subject_nr':'','age':0, 'handedness':('right','left','ambi'), #pasted original expInfo dict 
'gender':('male','female','other','prefer not to say')} 

expInfo['session']='1' #added variable 'session' equal to '1' 
expInfo['gender']=''   #changed gender to an empty box instead of a list using '' 

date = datetime.now()  #get current date & time, assign to variable date 
print(date)
expInfo['date']= str(date.day)+'/'+str(date.month)+'/'+str(date.year) #format date into day/month/year format 

dlg = gui.DlgFromDict(dictionary=expInfo, title = 'Subject Info',fixed='session', #added title to dlg 
order = ['session','subject_nr','age','gender','handedness'], show=False) 
#changed fixed from default None to 'session' to lock the session option (cannot be edited by subject) 
#changed order from default to determined order (shown above in list) 
#changed show to False so it does not show immedietly upon running

print('All variables have been created! Now ready to show the dialog box!') #print text before showing dlg 

showDlg = dlg.show() #trigger 'show' to reveal dialog box 

filename = str(expInfo['subject_nr'])+'_'+expInfo['date']+'.csv' #set filename as subject name from dialog box + current date 

mainDir = os.getcwd() #set main directory 
print(mainDir)
subDir = os.path.join(mainDir,'subjectInfo',filename) #create subdirectory titled 'subjectInfo' within mainDir containing filename listed above 
print(subDir)

##############################
# MONITOR & WINDOW EXERCISES 
############################## 
#1. The type of unit used determines how the size setting is interpreted - eg. 19x19 pix is much smaller than 19x19 cm 
    #Therefore, different units result in different window sizes
    #Units can also determine the stim size in the normalized units (height and norm) which change depending on monitor, or 
    #more specified units suich as cm or pix
    
#2. Changing the colorSpace determines which color system you use to translate color into numbers - eg. RBG, CMYK
    #Since computers have multiple systems to determine colour, this can be set using colorSpace
    #ex. if colorSpace is 'rbg', you may input 3 numbers to determine amount of red,green, and blue to set the color 
    #colors can also be defined by name or hex code 
    
from psychopy import visual, monitors 

mon1 = monitors.Monitor('laptopMonitor', width=31.00, distance = 60) #setup variable mon1 for my laptop monitor with measured width & distance
mon1.setSizePix([1920,1080]) #set pix based on laptop display 

window = visual.Window(monitor=mon1,size=(1920,1080),units='pix',fullscr=True,color=[0.78,0.63,0.78]) #create lilac fullscreen window size of laptop screen

