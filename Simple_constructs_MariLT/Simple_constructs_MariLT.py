#Task nr 1
print("Hello, World!") # like // in java 1 line comment till the end of line
'''like /*    .......    */ in java
This is a multiline comment in Python.
It can span multiple lines.
'''
name= input("Enter your name:").capitalize() #.lower()-aaa, .upper()-AAA, .capitalize() - Aaa
print("Welcome! Nice meeting you " , name)#adds space
print("Welcome! Nice meeting you " + name)
age= int(input("Enter your age: ")) 
print("Welcome! Nice meeting you " + name + " You are ", age, "years old.") #same type data can be added by +, if different types , if u use \t or \n they have to be inside ""
print(f"\tWelcome! \nNice meeting you {name}. You are  {age} years old.") 
print("\n")

#Task nr 2
age=18
firstName = "Jaak"
length = 16.5
goesToSchool = True
print ("",type(age),"\n",type(firstName),"\n",type(length),"\n",type(goesToSchool))
print("\n")

#Task nr 3
#from random import *(all functions) or from random import randint as rd(import or rename function)
import random
totalCandy= random.randint(1,1000)# totalCandy= randint(1,1000)
print(f"\nTotally on {totalCandy} candy")
candy= int(input("How much candy do you want to take?"))
print(f"Left {totalCandy-candy}") # or
# totalCandy=totalCandy-candy
# print(f"Left {totalCandy}")
print("\n")

#Task 4
from math  import *# to use Pi

#c-circumference
c=float(input("Enter tree circumference:"))
#d-diametr
d=c/pi
print(f"Diametr is approximately {round(d,2)}.")
print("\n")

#Task 5

#Calculate the length of the diagonal of a rectangular piece of land whose dimensions are 
#Nm x Mm using the Python calculator. Ask the user for N and M.

#N-diamension of a rectangular piece of land
N=float(input("Enter dimension N:"))
#M-diamension of a rectangular piece of land
M=float(input("Enter dimension M:"))
from math  import *# to use sqrt
#D-diagonal
D=sqrt(N*N+M*M)
print(f"Diametr is approximately {round(D,2)}.")
print("\n")

#Task 6

#Find a semantic error in the following example program:
time = float(input("How many hours did it take to drive? "))
distance = float(input("How many kilometres did you drive? "))
speed = distance/time

print("Your speed was " + str(speed) + " km/h")
print("\n")

#Task 7

#Write a program that calculates the arithmetic average of any given 5 integers.
#numbers - numbers inpited by user
print("Task: Find arithmetic average of 5 random numbers")
number0 = float(input("Enter first random number: "))
number1 = float(input("Enter second random number: "))
number2 = float(input("Enter third random number: "))
number3 = float(input("Enter fourth random number: "))
number4 = float(input("Enter fifth random number: "))
average = (number0+number1+number2+number3+number4)/5
print(f"Arithmetic average is {round(average,2)}.")
print("\n")

#Task 8
#Draw a frog like this
#    @..@
#   (----)
#  ( \__/ )
#  ^^ "" ^^
print("Let's draw a frog:\n")
print("    @..@\n")
print("   (----)\n")
print("  ( \__/ )\n")
print("   ^^ "" ^^\n")
print("Now we have a frog!")
print("\n")

#Task 9
#Let's calculate the perimeter of a triangle. 
#Create three integer variables a, b, c.
a=int(input("Enter first side of a triange:"))
b=int(input("Enter second side of a triange:")) 
c=int(input("Enter third side of a triange:")) 
#Create a formula that calculates the perimeter of a triangle (P=a+b+c).
P=a+b+c
print(f"Triangle perimetr equals {P}")
print("\n")

#Task 10
#Pizza
# You and a friend P have a large pizza for 12,90€.
# You leave a 10% tip for the waiter
# Create a program that finds how much everyone has to pay
price=12.9
#P_paid-how much friend paid for pizza
P_paid=price/2
#I_paid-how much I paid for pizza
I_paid=P_paid+price*0.1
print(f"Pizza price is {price} EUR")
print(f"I paid {I_paid} EUR for pizza and my friend P paid {P_paid} EUR for pizza")


