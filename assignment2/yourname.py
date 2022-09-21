# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:44:39 2022

@author: sasha schneider
"""

import numpy as np 

#############################
#PRINT & VARIABLE EXERCISES
#############################

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
print(letterX, letter3)


#############################
#BOOLEAN EXERCISES
#############################
 
print(1==1.0)
print('1'=='1.0')
print(5==(3+2))
 
#############################
#LIST EXERCISES
#############################

oddList = [1,3,5,7,9] #oddlist is now a variable 
print(oddList)
print(len(oddList)) 
#len of oddlist is 5 

print(type(oddList)) 
#oddlist is class 'list' 

inList = []
for n in range(0,101): #range expanded to 101 bc range stop is exclusive
    inList.append(n)
print(inList)


#############################
#DICTIONARY EXERCISES
#############################

aboutMe = {'name':'Sasha',
           'age':21.0,
           'yearOfStudy':5,
           'favFoods':['perogies','palak paneer','cheesecake']}

print(aboutMe)
print(type(aboutMe)) 
#class 'dict' 
print(len(aboutMe)) 
#len is 4
#len for dict is determined by number of key:value pairs

#####################################
#ARRAYS
#####################################

mixNums = np.array([3,6,9,
                    2.5,4.6,9.25])
print(mixNums)

mixTypes = np.array(['goose2',2,
                     10.5,12.25,4,
                     'goose1'])
print(mixTypes)

oddArray = np.arange(1,100,2) #begins at 1, steps 2 each time, ends at 100

logArray = np.logspace(1,5,16) #start = 1, stop = 5, n= 16 


