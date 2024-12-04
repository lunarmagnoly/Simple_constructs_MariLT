
#Task 1
name=input("Mis on sinu nimi? ")
if name.isalpha() and name.isupper():
    if name=="JUKU":
        print("Go for a movie")
        try:
            age=int(input(f"How old are you {name}?"))
            if   age<0:
                print("Logical error!")
            elif age<=6:
                print("Free!")
            elif age<15:
                print("Kinds ticket")
            elif age<65:
                print("Adult ticket")
            elif age < 100:
                print("Discount ticket")
            else:
                print ("That much?!")
        except:
             print("Wrong data, Integer awaited")   
             
# Task 2

name1=input("What is your name?")
name=input("What is your name?")
#1. variant

names=["Kirill","Gleb"]
if name1.isalpha() and name2isalpha():
    if( name1 in names) and(name2 in names):
        print("They are nrighbors")