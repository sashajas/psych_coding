###################################
OPERATION EXERCISES 
###################################


#1. Float division operations
print(5/2)
  returns 2.5;
print(5.0/2.0)
  returns 2.5 
  
same answer for both because / will always return a float 
to recieve a number in int form you need to use //

##################################################################


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

##################################################################


#4. Order of Operations
print(4+3+2*5/4) 
  returns 9.5
  
Yes, python does follow order of operations
  2*5 = 10, 10/4 = 2.5, 2.5+3+4 = 9.5 
