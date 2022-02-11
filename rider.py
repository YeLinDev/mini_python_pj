# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:49:37 2022

@author: Ye Lin Htet
"""

print("Welcome to MONSTER RIDER! Please enter the following detail : ")
age=int(input("What is the age of the first rider? : "))
height=int(input("What is the height of the first rider? : "))
yn=str(input("Is there a second rider (yes/no)? : "))

if height<36:
    print("Sorry, you may not ride.")
elif yn=="no" and age>=18 and height>=62:
    print("Welcome to the ride. Please be safe and have fun!")
elif yn=="yes" and age<18 and height<62:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")
    
    
    
##if ride:
## print("Welcome to the ride. Please be safe and have fun!")
##else:
##   print("Sorry, you may not ride.")