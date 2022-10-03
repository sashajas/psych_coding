# -*- coding: utf-8 -*-
"""
Assignment 3 - Sasha Schneider, 1598633

Due Oct 3

PSYCH 403 - Coding for Psychology 

* Lv 1: Manipulating Variables * 
"""

import numpy as np

######################
# variable operations 
###################### 

#1. 
subCode = 'sub'
subnrInt = 2 
subnrStr = "2"

print(subCode+subnrStr) 

#2. 
print(subCode+' '+subnrStr)
print(subCode+' '+subnrStr*3)
print((subCode+subnrStr)*3)
print(subCode*3+subnrStr*3)

######################
# list operations 
###################### 

#1. 
numList = [1,2,3]
print(numList*2)

#2. 
numArr = np.array([1,2,3])
print(numArr*2)

#3. 
strList = ['do','re','mi','fa']
dblList = [strList[0]*2,strList[1]*2,strList[2]*2,strList[3]*2]
dblListSep = [strList[0],strList[0], strList[1],strList[1],strList[2],strList[2],strList[3],strList[3]]
print(dblList)
print(strList*2)
print(dblListSep)
print(list(zip(strList,strList)))
print('\n')

######################
# zipping exercises 
###################### 

faces = ['faces1']*10 + ['faces2']*10 + ['faces3']*10 + ['faces4']*10 + ['faces5']*10 
houses = ['houses1']*10 + ['houses2']*10 + ['houses3']*10 + ['houses4']*10 + ['houses5']*10
cues = ['cue1']*25 + ['cue2']*25

combined = list(zip(faces,houses,cues))
import numpy as np
np.random.shuffle(combined)
print(combined)


######################
# indexing exercises
###################### 

#1. 
colors = ['red','orange','yellow','green','blue','purple']

#2. 
print(colors[-2])

#3. 
print(colors[-2][2],colors[-2][3])

#4. 
colors.remove('purple')
colors.append('indigo')
colors.append('violet')
print(colors)

######################
# slicing exercises
###################### 

#1. 
list100 = list(range(0,101))
print(list100)

#2. 
print(list100[:10])

#3. 
print(list100[99::-2])

#4. 
print(list100[101:96:-1])

#5. 
print(list100[40:45]==39,40,41,42,43) 
#No, they are not equal, because the first number is 0
#Therefore the 40th number is 40