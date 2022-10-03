
"""
PSYCH 403 - Coding for Psychology 
Lv 2 Exercises 

Assignment 4 - Conditionals and Loops 

Sasha Schneider, 1598633
"""

########################
# Conditional exercises 
########################

#1. & 2
userInput = input('What is your response?')

if userInput == '1' or userInput == '2': 
    if userInput == '1':
        print('Correct!')
    elif userInput == '2':
        print('Incorrect!')
elif userInput == 'NaN':
    print('Subject did not respond')
else: 
    print('Subject pressed wrong key')

#3. 
#The script acts as it is meant to, producing 'Correct!' for 1, 'Incorrect!' for 2, 
#'subject did not respond' if NaN is input, and 'subject pressed wrong key' for any other input

#########################
# Loop exercises
#########################

#1 & 2.
print('Exercises 1 & 2')
myName = 'Sasha'
counter = 0
for i in myName:
    print(i)
    print(counter)
    counter +=1

#3 & 4. 
print('Exercises 3 & 4')
names = ['Amy', 'Rory', 'River']

for indiv in names:
    index = 0
    for letter in indiv:
        print(letter)
        print(index)
        index += 1

#########################
# While loop exercises
#########################        
        
#1. 

counter = 0
while counter <20: 
    print(counter)
    if counter < 10:
        print('image1.png')
    elif counter >=10 and counter < 20:
        print('image2.png')
    counter +=1

#2 & 3. 
whileCounter = 0
while True:  
        if whileCounter >= 5: 
            break
        print('img.png')
        response = input('What is your response?')
        if response == '1' or response == '2':
            print('Correct!')
            break
        whileCounter += 1
        
        
    