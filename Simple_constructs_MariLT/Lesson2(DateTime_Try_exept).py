from datetime import *


#Task 1

today = date.today()
formatted_today0 = today.strftime("%B %d, %Y")
formatted_today1 = today.strftime("%d/%m/%Y")
formatted_today2 = today.strftime("%m/%d/%y")
formatted_today3 = today.strftime("%b-%d-%Y")
print(f"Hi! Today is {formatted_today0}")
print(f"Hi! Today is {formatted_today1}")
print(f"Hi! Today is {formatted_today2}")
print(f"Hi! Today is {formatted_today3}")

day = today.day
month = today.month
year= today.year
print(day)
print(month)
print(year)
from calendar import *

monthdays=monthrange(2024,11)[1]
countTillMonthEnd=int(monthdays-day)#till the end of mounth
print(f"Left till month end {countTillMonthEnd}")
countTillNewYear=int(monthrange(2024,12)[1]+countTillMonthEnd)
print(f"Left till the New Year {countTillNewYear} days")

#Task 2

answer0=3+8 / (4-2)*4
answer1=3+8 / 4-2 * 4
answer2=(3+8)/(4-2)*4
print(f"{answer0} \n{answer1} \n{answer2}")
from math import *

#Task 3

# var1
try:
    R=float(input("Input R"))
    Sk=pi*R**2
    Lk=2*pi*R
    Skv=(2*R)**2
    Lkv=2*R*4
    print(f"Ringi pindala on {Sk}\nRingi umbermoot om {Lk}\nRuudu pindala on {Skv:}\n Ruudu umbermoot on {Lkv}")

except:
    print("It has to be a number!")

from random import *
#var 2
R=round(random()*100)# 0.0 ..... 1.0
Sk=pi*R**2
Lk=2*pi*R
Skv=(2*R)**2
Lkv=2*R*4
print(f"Ringi pindala on {Sk}\nRingi umbermoot om {Lk}\nRuudu pindala on {Skv:}\n Ruudu umbermoot on {Lkv}")



#Task 4
