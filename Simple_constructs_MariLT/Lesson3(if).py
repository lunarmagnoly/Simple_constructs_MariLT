
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
#Task 4
#Find the price with a 30% discount if the original price is more than 700.

# try:
#     price=float(input("Enter price: "))
#     if price>=700:
#         discount=30/100 #-30%
#         price-=price*discount
#         print(f"New price after discount is {price} €")
#     else:
#         print(f"Doesn't have discount. Price stays the same {price} € ")
# except:
#     print("Error. Enter only numbers")
# print("\n")
# #Task 5
# #Ask for the temperature and report if it is over 18 degrees (recommended indoor temperature in winter).

# try:
#     temp=float(input("Enter indoor temperature in °C "))
#     if 18 < temp < 25:
#         print("Indoor temperature is in reccomended range")
#     else:
#         print("Recomended indoor temperature is in the range of 18 - 25 °C")
# except:
#     print("Error. Check if text is numbers")
# print("\n")

#Task 6
#Ask for the person's height and report whether they are short, average, or tall (set the boundaries yourself).
# try:
#     height=float(input("Enter you height in cm please "))

#     if height < 54.6:
#         print("Extremely short. You might either be a hidden Guinness World Record holder or there could be a typo.")
#     elif height<165:
#         print("You are short")
#     elif 165 <= height < 175:
#         print("You are short for male, but average for female")
#     elif height==175:
#         print("Your height is average")
#     elif 175 < height <= 185:
#         print("You are tall for female, but average for male")
#     else:
#         print("You are tall")

# except:
#     print("Error. Height mus be in cm and nummeric")
# print("\n")

#Task 7
#Ask a person their height and gender, and then tell them if they are short, average, or tall 
#(multiple conditional blocks may be nested).

# try:
    
#     gender=input("Enter your gender(m/f): ")
#     height=float(input("Enter you height in cm please "))

#     if gender.lower()=="m" and height < 175:
#         print("You are short")
#     elif gender.lower()=="m" and 175 <= height <= 185:
#         print("You are average")
#     elif gender.lower()=="m" and height > 185:
#         print("You high")
#     elif gender.lower()=="f" and height < 165:
#         print("You are short")
#     elif gender.lower()=="f" and 165 <= height <= 175:
#         print("You are average")
#     else:
#         print("You are tall")
# except:
#     print("Error. Height mus be in cm and nummeric")
# print("\n")
#Task 8
#Individually ask a person in a store if they want to buy milk, buns, bread, etc. 
#Generate random prices and ask how many they want to buy if they choose to. 
#Report the total amount they have to pay (Display the receipt on the screen).

