
# #Task 1

# name=input("Mis on sinu nimi? ")
# if name.isalpha() and name.isupper():
#     if name=="JUKU":
#         print("Go for a movie")
#         try:
#             age=int(input(f"How old are you {name}?"))
#             if   age<0:
#                 print("Logical error!")
#             elif age<=6:
#                 print("Free!")
#             elif age<15:
#                 print("Kinds ticket")
#             elif age<65:
#                 print("Adult ticket")
#             elif age < 100:
#                 print("Discount ticket")
#             else:
#                 print ("That much?!")
#         except:
#              print("Wrong data, Integer awaited")   

# print("\n")         

# # Task 2

# name1=input("What is your name?")
# name2=input("What is your name?")
# #1. variant

# names=["Kirill","Gleb"]
# if name1.isalpha() and name2.isalpha():
#     if( name1 in names) and(name2 in names):
#         print("They are neighbors")
#     else:
#         print("They are from one group")

# print("\n")

# #Task 3

# try:
#     a=float(input("Room lenght: "))
#     b=float(input("Room width: "))
#     S=a*b
#     print(f"Floor area is {S} m**2")
#     answer=input("Would you like to do renovation?(Yes-1/No-0) ") #Jah/ei JAH, jah
#     if answer.upper()=="YES" or answer =="1":
#         print("Renovation")
#         price=float(input("One meeter price: "))
#         summ=price*S
#         print(f"Renovation costs {summ} €")
#     elif answer.upper()=="NO" or answer ==0:
#         print("-")
#     else:
#         print("Don't understand")
# except:
#     print("Numbers!")

# print("\n")

# Task 4
# Find the price with a 30% discount if the original price is more than 700.

try:
    price=float(input("Enter price: "))
    if price>=700:
        discount=30/100 #-30%
        price-=price*discount
        print(f"New price after discount is {price} €")
    else:
        print(f"Doesn't have discount. Price stays the same {price} € ")
except:
    print("Error. Enter only numbers")
print("\n")
#Task 5
#Ask for the temperature and report if it is over 18 degrees (recommended indoor temperature in winter).

try:
    temp=float(input("Enter indoor temperature in °C "))
    if 18 < temp < 25:
        print("Indoor temperature is in reccomended range")
    else:
        print("Recomended indoor temperature is in the range of 18 - 25 °C")
except:
    print("Error. Check if text is numbers")

print("\n")

# Task 6
# Ask for the person's height and report whether they are short, average, or tall (set the boundaries yourself).

try:
    height=float(input("Enter you height in cm please "))

    if height < 54.6:
        print("Extremely short. You might either be a hidden Guinness World Record holder or there could be a typo.")
    elif height<165:
        print("You are short")
    elif 165 <= height < 175:
        print("You are short for male, but average for female")
    elif height==175:
        print("Your height is average")
    elif 175 < height <= 185:
        print("You are tall for female, but average for male")
    else:
        print("You are tall")

except:
    print("Error. Height mus be in cm and nummeric")

print("\n")

# Task 7
# Ask a person their height and gender, and then tell them if they are short, average, or tall 
# (multiple conditional blocks may be nested).

try:
    
    gender=input("Enter your gender(m/f): ")
    height=float(input("Enter you height in cm please "))

    if gender.lower()=="m" and height < 175:
        print("You are short")
    elif gender.lower()=="m" and 175 <= height <= 185:
        print("You are average")
    elif gender.lower()=="m" and height > 185:
        print("You high")
    elif gender.lower()=="f" and height < 165:
        print("You are short")
    elif gender.lower()=="f" and 165 <= height <= 175:
        print("You are average")
    else:
        print("You are tall")
except:
    print("Error. Height mus be in cm and nummeric")

print("\n")

# Task 8
# Individually ask a person in a store if they want to buy milk, buns, bread, etc. 
# Generate random prices and ask how many they want to buy if they choose to. 
# Report the total amount they have to pay (Display the receipt on the screen).

import random

try:
    milk_price=round(random.uniform(0.5, 3.0),2)
    print(f"One pack of milk costs {milk_price} €\n")
    milk=input("\nWould you like to buy milk?(y/n) ")
    
    total_cost=0.0
    milk_total_price = 0.0

    if milk.lower() == "y":
        milk_number=int(input("How many packs of milk would you like? " ))
        milk_total_price=milk_price*milk_number
        print(f"Milk would cost you {round(milk_total_price, 2)} €")
        total_cost+=milk_total_price
        print(f"\n\nTotal cost is {round(total_cost, 2)} €")
    
    white_bread_price=round(random.uniform(0.5, 2.0),2)
    print(f"\nOne pack of white bread costs {white_bread_price} €\n")
    white_bread=input("\nWould you like to buy white bread(y/n)? ")
    white_bread_total_price=0.0

    if white_bread.lower() == "y":
            white_bread_number=int(input("How many packs of white bread would you like? " ))
            white_bread_total_price=white_bread_number*white_bread_price
            print(f"White bread would cost you {round(white_bread_total_price,2)} €")
            total_cost+=white_bread_total_price
            print(f"\n\nTotal cost is {round(total_cost, 2)} €")
    
    rye_bread_price=round(random.uniform(0.5, 2.0), 2)
    print(f"\nOne pack of rye bread costs {rye_bread_price} €\n")
    rye_bread=input("\nWould you like to buy rye bread(y/n)? ")
    rye_bread_total_price=0.0
    
    if rye_bread.lower() == "y":
            rye_bread_number=int(input("How many packs of rye bread would you like? " ))
            rye_bread_total_price=rye_bread_number*rye_bread_price
            print(f"Rye bread would cost you {round(rye_bread_total_price, 2)} €")
            total_cost+=rye_bread_total_price
            print(f"\n\nTotal cost is {round(total_cost, 2)} €")
    
    print("\n")
     
    line="|----------------------------------------------------------------------------------------------------------------------|\n"
    heading="|\t\t\t\t\t\t\tReceipt \t\t\t\t\t\t\t\t|\n"
    definition_line="|\tProduct name\t|\tNumber of products\t|\tPrice of one\t|\tTotal price for product \t|\n"
        
    print(line+heading+line+definition_line+line) 
    
    if milk_total_price > 0:
        milk_line=f"|\tMilk\t\t|\t{milk_number}\t\t\t|\t{round(milk_price,2)} €\t\t|\t\t{round(milk_total_price,2)} €\t\t\t|\n"
        print(milk_line)
       
    if white_bread_total_price > 0: 
        white_bread_line=f"|\tWhite Bread\t|\t{white_bread_number}\t\t\t|\t{round(white_bread_price,2)} €\t\t|\t\t{round(white_bread_total_price,2)} €\t\t\t|\n"
        print(white_bread_line)
    
    if rye_bread_total_price > 0:
        rye_bread_line=f"|\tRye Bread\t|\t{rye_bread_number}\t\t\t|\t{round(rye_bread_price,2)} €\t\t|\t\t{round(rye_bread_total_price,2)} €\t\t\t|\n"
        print(rye_bread_line)
    
    total_line=f"|\t\t\t\t\t\t\t\t\t\t\tTotal: {round(total_cost, 2)} €\t\t\t|\n"

    print(line+total_line+line)    
except:
    print("Error. Might be input typo")
    
print("\n")        

#Task 9
#The user inputs the sides of a square, and the program detects whether it can be a square. 
#Create the corresponding block diagram and save it in the same directory as the program.

try:
    print("Insert figure sides in same unit of lenght:")    
    side_A=float(input("\nEnter side A "))    
    side_B=float(input("Enter side B "))
    side_C=float(input("Enter side C "))
    side_D=float(input("Enter side D "))
    
    if side_A==side_B==side_C==side_D:
        print("\nThe figure is a square.")
    else:
        print("The figure is not a square or there is a typo.")
except:
    print("Lenght should be a number")

print("\n")

#Task 10
#The user inputs two numbers, and the program asks the user which operation they want to perform (+, -, *, /) and executes the user's choice. 
#Create the corresponding block diagram and save it in the same directory as the program.

try:
    num0, num1 = map(float, input("Enter two numbers separated by a space: ").split())
    operation=input("Choose operation to perform (+, -, *, /): ")
    if operation=="+":
        result=num0+num1
    elif operation=="-":
        result=num0-num1
    elif operation=="*":
        result=num0*num1
    elif operation=="/":
        result= num0/num1
    print(f"Result is equal {result}")
except:
    print("Error. There must be a typo.")

print("\n") 

#Task 11
#The user inputs their birthdate, and your program tells whether it is a milestone anniversary. 
#No need for a block diagram!

from datetime import datetime
try:
    birthday = datetime.strptime(input("Enter your birthday (DD.MM.YYYY) "), "%d.%m.%Y").date()
    today = datetime.today().date()
    age=today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    if age%10==0:
        print("Happy anniversary!")
    elif age%10!=0:
        print("Maybe next year")
except ValueError:
    print("There must be a typo")

print("\n")

#Task 12
#The user inputs the product price. If the price is up to 10€, they get a 10% discount. 
#Products over 10€ get a 20% discount. Display the final price of the product. 
#No need for a block diagram!

try:
    price=float(input("Enter price "))

    if price<=10:
        discount=price*0.1
    elif price>10:
        discount=price*0.2
    
    price-=discount
    print(f"Price after discount is {price} € ")

except:
    print("Typo")

print("\n")

#Task 13
#You need to create a program that checks if an applicant is suitable for the team. 
#The age must be between 16-18 and only males are allowed. 
#Enhance the program so that if the applicant is female, the age is not asked at all.

from datetime import datetime
try:
    gen=input("Enter gender(m/f) ")
    
    if gen.lower() == "m":
        birthday = datetime.strptime(input("Enter your birthday (DD.MM.YYYY) "), "%d.%m.%Y").date()
        today = datetime.today().date()
        age=today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        
        if 16 <= age <= 18:
            print("Suitable for the team")
        else:
            print("Not suitable for the team")
    else:
        print("Not suitable for the team")

except:

    print("Typo")

print("\n")

#Task 14
#Let's say we need to transport a certain number of people using buses that have a certain number of seats. 
#How many buses are needed to transport all the people, and how many people are in the last bus 
#(assuming all previous buses are completely full)? 
#Write a program that asks for the number of people and the bus size, then solves this problem.

try:
    people=int(input("Insert number of people that need transportation "))
    bus_seats=int(input("Insert number of seats in each "))
    buses_number=people//bus_seats
    last_bus_people=people % bus_seats
    if last_bus_people>0 :
        buses_number+=1
    else:
        last_bus_people = bus_seats

    print(f"We need {buses_number} buses and last one has {last_bus_people} people")
except:
    print("Typo")
