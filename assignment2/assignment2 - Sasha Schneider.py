# -*- coding: utf-8 -*-
"""
PSYCH 403 Coding for Psychology

Note: Rather than creating many small files, I put all in a single readable file 

Hopefully this is okay! 
Please send me an email at sasha1@ualberta.ca if you would prefer assignments in many small files

@author: sasha schneider
"""

import numpy as np 

#############################
#PRINT & VARIABLE EXERCISES
#############################

print('PRINT AND VARIABLE EXERCISES\n')

letter1 = 's'
letterX = 'a'
letter3 = 's'
letter4 = 'h'
letter5 = 'a'


for l in 'sasha':
    print(l)
    
print(letterX, letter5)

letterX = 'b'
print(letterX, letter5)

letterX = letter3
print(letterX, letter3)

letter3 = 'z'
print(letterX, letter3,'\n')


#############################
#BOOLEAN EXERCISES
#############################
print('BOOLEAN EXERCISES\n')

print(1==1.0)
print('1'=='1.0')
print(5==(3+2),'\n')
 
#############################
#LIST EXERCISES
#############################
print('LIST EXERCISES\n')

oddList = [1,3,5,7,9] #oddlist is now a variable 
print('oddList:')
print(oddList)
print(len(oddList)) 
#len of oddlist is 5 

print(type(oddList)) 
#oddlist is class 'list' 

inList = []
for n in range(0,101): #range expanded to 101 bc range stop is exclusive
    inList.append(n)
    
print('inList:')
print(inList,'\n')


#############################
#DICTIONARY EXERCISES
#############################
print('DICTIONARY EXERCISES\n')

aboutMe = {'name':'Sasha',
           'age':21.0,
           'yearOfStudy':5,
           'favFoods':['perogies','palak paneer','cheesecake']}
print('aboutMe dict:')
print(aboutMe)
print(type(aboutMe)) 
#class 'dict' 
print(len(aboutMe),'\n') 
#len is 4
#len for dict is determined by number of key:value pairs

#####################################
#ARRAYS
#####################################
print('ARRAY EXERCISES\n')

mixNums = np.array([3,6,9,
                    2.5,4.6,9.25])
print('mixNums:')
print(mixNums)

mixTypes = np.array(['goose2',2,
                     10.5,12.25,4,
                     'goose1'])
print('mixTypes:')
print(mixTypes)

oddArray = np.arange(1,100,2) #begins at 1, steps 2 each time, ends at 100

logArray = np.logspace(1,5,16) #start = 1, stop = 5, n= 16 


