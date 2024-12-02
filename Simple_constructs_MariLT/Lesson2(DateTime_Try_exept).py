# from datetime import *


# #Task 1

# today = date.today()
# formatted_today0 = today.strftime("%B %d, %Y")
# formatted_today1 = today.strftime("%d/%m/%Y")
# formatted_today2 = today.strftime("%m/%d/%y")
# formatted_today3 = today.strftime("%b-%d-%Y")
# print(f"Hi! Today is {formatted_today0}")
# print(f"Hi! Today is {formatted_today1}")
# print(f"Hi! Today is {formatted_today2}")
# print(f"Hi! Today is {formatted_today3}")

# day = today.day
# month = today.month
# year= today.year
# print(day)
# print(month)
# print(year)
# from calendar import *

# monthdays=monthrange(2024,11)[1]
# countTillMonthEnd=int(monthdays-day)#till the end of mounth
# print(f"Left till month end {countTillMonthEnd}")
# countTillNewYear=int(monthrange(2024,12)[1]+countTillMonthEnd)
# print(f"Left till the New Year {countTillNewYear} days")

# print("\n")

# #Task 2

# answer0=3+8 / (4-2)*4
# answer1=3+8 / 4-2 * 4
# answer2=(3+8)/(4-2)*4
# print(f"{answer0} \n{answer1} \n{answer2}")
# from math import *

# print("\n")

# #Task 3

# # var1
# try:
#     R=float(input("Input R "))
#     Sk=pi*R**2
#     Lk=2*pi*R
#     Skv=(2*R)**2
#     Lkv=2*R*4
#     print(f"Ringi pindala on {Sk}\nRingi umbermoot om {Lk}\nRuudu pindala on {Skv:}\nRuudu umbermoot on {Lkv}")

# except:
#     print("It has to be a number!")
    


# from random import *
# #var 2
# R=round(random()*100)# 0.0 ..... 1.0
# Sk=pi*R**2
# Lk=2*pi*R
# Skv=(2*R)**2
# Lkv=2*R*4
# print(f"Ringi pindala on {Sk}\nRingi umbermoot on {Lk}\nRuudu pindala on {Skv}\nRuudu umbermoot on {Lkv}")

# print("\n")

# #Task 4
# d=2.575 #coin d
# earth=6378#earth radius in km
# earth*=100000# earth radius in cm same as earth=earth*100000
# Learth=2*pi*earth
# num=Learth/d
# print(f"It takes {num} coins.\nWe would need {num*2} EUR")

# print("\n")

#Task 5
#Using your previous knowledge, write a program that would output:
#kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll kill-koll
#kill-koll


#Variables can be used. Display each word with a capital letter.

a="kill".capitalize()
b="koll".capitalize()
c="killadi".capitalize()

print (f"{a}-{b} {a}-{b} {c}-{b} {a}-{b} {a}-{b} {c}-{b} {a}-{b} {a}-{b} {a}-{b} \n{a}-{b}")

print("\n")

#Task 6
''' Create a program that would output the following lyrics in capital letters:

Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill. 

....Input, Output, Condition....'''

while True:
    try:
        a=input("Would you like to read a poem? ")
        if a.lower()=="yes":
             print("\n")
             text="Rong see sõitis tsuhh tsuhh tsuhh,\npiilupart oli rongijuht.\nRattad tegid rat tat taa,\nrat tat taa ja tat tat taa.\nAga seal rongi peal,\nkas sa tead, kes olid seal?\n\nRong see sõitis tuut tuut tuut,\npiilupart oli rongijuht.\nRattad tegid kill koll koll,\nkill koll koll ja kill koll kill.".upper()
             print(text)
             break
        else:
             print("Enter Yes if you would like to read the poem")
    except:
           print("Input has to be a word")
           continue
print("\n")
# Task 7 
# Create a program that asks the user for the lengths of the sides of a rectangle and 
# then outputs the perimeter and area of the rectangle on the screen.
while True:
    try:
        a=float(input("Enter lenght of first rectangle side in cm "))
        b=float(input("Enter lenght of second rectangle side in cm "))
        P=2*(a+b)
        S=a*b
        print(f"Rectangle Perimetr is {P} cm\nRectangle Area is {S} cm")
        break
    except:
        print("Wrong data entered, enter number")

print("\n")

#Task 8 
#Fuel Consumption Calculation
#   The user inputs the amount of refueled fuel in liters 
#   The user inputs the distance traveled in kilometers 
#   The program calculates the average fuel consumption per 100 km
while True:
    try:
        fuel=float(input("Enter refueld fuel in liters "))
        distance=float(input("Enter traveled distance in kilometers "))
        average_fuel_per_100km=(fuel/distance)*100
        print(f"Average fuel consumption per 100 kilometers is {average_fuel_per_100km}")
        break
    except:
        print("Fuel and distance are numbers")
print("\n")
#Task 9 Roller Skaters
#The average speed of a roller skater is 29.9 km/h
#How far will they travel in M minutes?

while True:
    try:
        time=float(input("How long did roller scaters traveled?\nEnter in minutes: "))
        speed=29.9#km/h
        distance=time/60*speed
        print(f"Roller scaters traveled {round(distance,2)} kilometers")
        break
    except:
        print("Time is entered as number in minutes")
print("\n")
#Task 10
#Timeline
# User enters time in minutes
# Your formula finds and outputs hours and minutes
# For example: input 72, answer 1:12
while True:
    try:
        time=int(input("Enter time period in minutes "))
        hours=time//60
        minutes_left=time%60
        print(f"Converted time is {hours} hours and {minutes_left} minutes")
        break
    except:
        print("Time has to be entered as number")
