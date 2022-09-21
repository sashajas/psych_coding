########################
OPERATION EXERCISES 
########################

#1. Float division operations
print(5/2)
  returns 2.5;
print(5.0/2.0)
  returns 2.5 
  
same answer for both because / will always return a float 
to recieve a number in int form you need to use //

#######################################


#2. Modulo operations
print(2%5)
  returns 2;
print(4%16)
  returns 4;
print(8%126)
  returns 8
  
molulo operator determines the remainder of division
  i.e. how many times does 4 fit into 16 evenly (answ:4)

##################################################################

#3.

a) Int division operations

print(12//2)
  returns 6;
print(4//2)
  returns 2;
print(15//3)
  returns 5
  
dividing using // will divide the left number by right
  then return the value as a rounded int 
 

b) Int Power operations

print(3**2)
  returns 9;
print(5**2)
  returns 25;
print(3**3)
  returns 27
  
 rather than multiplying using *, operations using **
  calculates (left number) to the power of (right number)

##############################################


#4. Order of Operations
print(4+3+2*5/4) 
  returns 9.5
  
Yes, python does follow order of operations
  2*5 = 10, 10/4 = 2.5, 2.5+3+4 = 9.5 


###########################
VARIABLE EXERCISES
###########################

#2. all variables are listed in Variable Editor as labelled 

#4. letter2 ('a') reassigned to letterX ('a'), with letter5 remaining 'a'

  letter2 still assigned same letter in Variable Editor, letterX and letter5 both assigned to 'a'
  - Python has no issue with multiple variables having same value 

#5. letterX assigned 'b' - changing letterX did not change other variables 

#6. letterX assigned to letter3 ('s'), letterX now prints as 's'; 
letter3 reassigned to 'z'; 
letter3 now prints 'z', letterX still prints 's'

NOTE: if letterX were assigned letter3 again, it would then print as 'z' 

Python assigns variables in corresponding space in memory banks - when letterX was assigned to the same string value as letter3, it stopped connecting to 'a' and now linked to 's';
However, when letter3 changed, letterX remained linked to 's' - variables change only when specifically assigned to do so 

#########################
BOOLEAN EXERCISES
#########################

#1. 
1 and 1.0 are equivalent, regardless of format - python returns True
'1' and '1.0' are not equivalent - in str format they are no longer numbers, thus python evaluates them not in terms of numerical value, but whether the strings are identical 

#2. 
Yes, 5 and (3+2) are equivalent - their numerical values are identical once 3+2 has been added

#3. [Are 1 and 1.0 equivalent?] and not [Are '1' and '1.0' equivalent?] or [Are 5 and (3+2) equivalent?] (Note-question is difficult to understand..) 
1 == 1.0 returns True;
'1' != '1.0' returns True;
5 > 1 returns True;
5 == (3+2) returns True;
5 != 1 returns True 

######################
ARRAY EXERCISES
######################

#1. The array is printed spaced apart (separated by '.') and ordered as was input

#2. The array is seperated instead by '' but remains in input order - this was verified by ordering the array with a string at the beginning and end
  - When printed, the array was not reordered 
