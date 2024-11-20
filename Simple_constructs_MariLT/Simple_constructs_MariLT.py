#Task nr 1
# print("Hello, World!") # like // in java 1 line comment till the end of line
# '''like /*    .......    */ in java
# This is a multiline comment in Python.
# It can span multiple lines.
# '''
# name= input("Enter your name:").capitalize() #.lower()-aaa, .upper()-AAA, .capitalize() - Aaa
# print("Welcome! Nice meeting you " , name)#adds space
# print("Welcome! Nice meeting you " + name)
# age= int(input("Enter your age: ")) 
# print("Welcome! Nice meeting you " + name + " You are ", age, "years old.") #same type data can be added by +, if different types , if u use \t or \n they have to be inside ""
# print(f"\tWelcome! \nNice meeting you {name}. You are  {age} years old.") 

# #Task nr 2
# age=18
# firstName = "Jaak"
# length = 16.5
# goesToSchool = True
# print ("",type(age),"\n",type(firstName),"\n",type(length),"\n",type(goesToSchool))

# #Task nr 3
# #from random import *(all functions) or from random import randint as rd(import or rename function)
# import random
# totalCandy= random.randint(1,1000)# totalCandy= randint(1,1000)
# print(f"\nTotally on {totalCandy} candy")
# candy= int(input("How much candy do you want to take?"))
# print(f"Left {totalCandy-candy}") # or
# # totalCandy=totalCandy-candy
# # print(f"Left {totalCandy}")

#Task 4
from math  import *# to use Pi

#c-circumference
c=float(input("Enter tree circumference:"))
#d-diametr
d=c/pi
print(f"Diametr is approximately {round(d,2)}.")

