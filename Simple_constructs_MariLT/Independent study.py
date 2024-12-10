
#Task 1 
#The user enters a number, and the program determines the sign of the number (whether it is positive or negative). 
#If the number is positive, it checks whether it is even or odd.
try:
    num=int(input("Enter integer number "))
    if num > 0:
    
        if num%2==0:
            print("Number is positive and even")
        else:
            print("Number is positive and odd")
    elif num < 0:
        print("Number is negative")
except:
    print("Typo")

print("\n")

#Task 2
#Ask the user for 3 numbers. 
#If they are positive, check if they can be the angles of a single triangle (the sum of the angles is 180). 
#Then determine what type of triangle they form (equilateral, isosceles, or scalene).
import math
try:
    side_A=float(input("Enter first side "))
    side_B=float(input("Enter second side "))
    side_C=float(input("Enter third side "))
    if side_A > 0 and side_B > 0 and side_C > 0:
        print("\nSides values are positive")
        if side_A + side_B > side_C and side_A + side_C > side_B and side_B + side_C > side_A:
            
            print("\nFigure is a triangle\n")
            cos_a=(side_A**2+side_C**2-side_B**2)/(2*side_A*side_C)
            angle_a = round(math.degrees(math.acos(cos_a)), 2)
            print(f"Angle a {angle_a} degrees\n")
        
            cos_b=(side_A**2+side_B**2-side_C**2)/(2*side_A*side_B)
            angle_b = round(math.degrees(math.acos(cos_b)), 2)
            print(f"Angle b {angle_b} degrees\n")
        
            cos_c=(side_B**2+side_C**2-side_A**2)/(2*side_B*side_C)
            angle_c = round(math.degrees(math.acos(cos_c)), 2)
            print(f"Angle c {angle_c} degrees\n")

            if side_A==side_B==side_C:
                    print("Figure is equilateral triangle")

            elif side_A==side_B or side_C==side_B or side_A==side_C:
                    print("Figure is Isosceles triangle")
            else:
                print("Figure is Scalene triangle")
        else:
            print("Not a triangle")
    else:
        print("Figure sides can't be equal 0 or less ")

except:
    print("Typo")

print("\n")

#Task 3
#Find out if the user wants to convert a day of the week number into its name. 
#If the user answers "yes" (consider that the user may answer in lowercase or uppercase), ask for a number. 
#If the number is from 1 to 7, display the corresponding day of the week.

try:
    question=input("Would you like to convert a day of the week number into its name? (Yes/No) ")

    if question.lower()=="yes":
        number=int(input("\nWhat number you would like to convert? (1-7) "))

        print("\n")

        if number == 1:
            
            print("Monday")
        
        elif number ==2:

            print("Tuesday")

        elif number == 3:

            print("Wednesday")
    
        elif number == 4:

            print("Thursday")

        elif number == 5:

            print("Friday")

        elif number == 6:

            print("Saturday")            

        elif number == 7:

            print("Sunday")
except:

    print("Typo")

print("\n")

#Task 4
#Determine the user's zodiac sign based on their birth day and month. 
#Validate the entered data (data type and range of values), and if the data is invalid, display an appropriate message.

from datetime import datetime

try:
    birthday = datetime.strptime(input("Enter your birthday (DD.MM) "), "%d.%m").date()
    day = birthday.day 
    month = birthday.month
    
    if (month == 1 and day >= 20) or (month == 2 and day <= 18): zodiac = "Aquarius" 
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20): zodiac = "Pisces" 
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19): zodiac = "Aries" 
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20): zodiac = "Taurus" 
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20): zodiac = "Gemini" 
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22): zodiac = "Cancer" 
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22): zodiac = "Leo" 
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22): zodiac = "Virgo" 
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22): zodiac = "Libra" 
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21): zodiac = "Scorpio" 
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21): zodiac = "Sagittarius" 
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19): zodiac = "Capricorn"

    print(f"\nYour zodiac sign is: {zodiac}")

except:

    print("Typo")

print("\n")

#Task 5
#Check the number entered by the user, determine its type, and if the number is an integer, find 50% of it. 
#If the number is a fractional number, find 70% of it. 
#If it is text, display it on the screen. You can use is_integer(), isalpha(), isdigit(), int(), float(), //, and % for the solution.

try:
    entery = input("Enter something ")
    number = float(entery)
    
    if number.is_integer(): 
        result = round(number*0.5, 2 )
        print(f"\n50 % of Integer is approximetly {result} ")
        
    else:
        result = round(number*0.7, 2 )
        print(f"70 % of Fractional number is approximetly {result}")

except ValueError :
    
    if entery.isalpha():
        print(f"{entery}")

    else: 
        
        print("Typo")


print ("\n")            

#Task 6
#Write a program to solve the quadratic equation a*x**2+b*x+c=0.
#First, ask if the user wants to solve the equation, and only after a positive response, ask for the values of a,b and c.
#If the user does not want to solve the equation, say goodbye to the user.
#Find 𝐷: 𝐷=b**2-4ac
#If 𝐷 > 0, there are 2 solutions:
#                               x1=(-b+D**1/2)2a
#                               x2=(-b-D**1/2)2a
#If 𝐷 = 0, there is 1 solution:
#                               x=-b/2a
#If 𝐷 < 0, there are no solutions.
#Round the answers to 2 decimal places.

import math

try:
    question=input("Would you like to solve the quadratic equation?(Yes/No) ")
    
    if question.lower()=="yes":
        
        a=float(input("Enter a "))
        b=float(input("Enter b "))
        c=float(input("Enter c "))

        D = b**2-4*a*c
        
        if D > 0:
            
            sqrt=math.sqrt
            x1 = (-b+sqrt(D))/2*a
            x2 = (-b-sqrt(D))/2*a
            
            print(f"Quadratic equation has 2 solutons: {x1} and {x2}")

        elif D == 0:

            x=-b/(2*a)

            print(f"Quadratic equation has 1 soluton: {x} ")

        elif D < 0:

            print("Quadratic equation has no solutons")
      
    elif question.lower()=="no":

        print("Goodbye")
except:
    print("Typo")

print ("\n")        



