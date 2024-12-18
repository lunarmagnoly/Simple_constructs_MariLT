#Write a program for testing mathematical knowledge.
import random
# Offer the user to choose the difficulty level of the tasks. For example:
level=input("Choose complexity level(1,2,3): ")
# The number of operations (+, -, /, *, **)
operations_count=input("Choose number of operations (+, -, /, *, **): ")
# The range of randomly generated numbers.
number_range=input("Choose range of randomly generated numbers: ")
count=0
tasks_number=0
#use .split() or .split(',') first if parse by space second if by ,
# result=count/tasks_number*100
#     if result <60:
#         print("Grade : 2")
#     elif 60<=result<75:
#         print("Grade : 3")
#     elif 75<=result<=90:
#         print("Grade : 4")
#     elif result>90:
#         print("Grade : 5")

# Level 1 (Tase 1)
if level == "1":
    number1=random.randint(1, 10)
    number2=random.randint(1, 10)
    task0=float(input(f"Solve:\n{number1} + {number2} = "))
    if task0 == number1+number2:
        count+=1
    else: count=0
    task1=float(input(f"Solve:\n{number1} - {number2} = "))
    if task1 == number1-number2:
        count+=1
    else: count=0
    task2=float(input(f"Solve:\n{number1} * {number2} = "))
    if task2 == number1*number2:
        count+=1
    else: count=0
    task3=float(input(f"Solve:\n{number1} / {number2} = "))
    if task3 == number1/number2:
        count+=1
    else: count=0
    task4=float(input(f"Solve:\n{number1} ^ {number2} = "))
    if task4 == number1 ** number2:
        count+=1
    else: count=0
    
    

# Level 2 (Tase 2)

elif level == 2:
    number1=random.randint(1, 50)
    number2=random.randint(1, 50)
    number3=random.randint(1, 50)
    number4=random.randint(1, 50)

    task0=float(input(f"Solve:\n{number1} + {number2} = "))
    if task0 == number1+number2:
        count+=1
    else: count=0
    task1=float(input(f"Solve:\n{number1} - {number2} = "))
    if task1 == number1-number2:
        count+=1
    else: count=0
    task2=float(input(f"Solve:\n{number1} * {number2} = "))
    if task2 == number1*number2:
        count+=1
    else: count=0
    task3=float(input(f"Solve:\n{number1} / {number2} = "))
    if task3 == number1/number2:
        count+=1
    else: count=0
    task4=float(input(f"Solve:\n{number1} ^ {number2} = "))
    if task4 == number1 ** number2:
        count+=1
    else: count=0
    
    result=count/5*100
    if result <60:
        print("Grade : 2")
    elif 60<=result<75:
        print("Grade : 3")
    elif 75<=result<=90:
        print("Grade : 4")
    elif result>90:
        print("Grade : 5")

# Level 3 (Tase 3)

elif level == 3:

    number1=random.randint(1, 50)
    number2=random.randint(1, 50)
    number3=random.randint(1, 50)
    number4=random.randint(1, 50)

    task0=float(input(f"Solve:\n{number1} + {number2} = "))
    if task0 == number1+number2:
        count+=1
    else: count=0
    task1=float(input(f"Solve:\n{number1} - {number2} = "))
    if task1 == number1-number2:
        count+=1
    else: count=0
    task2=float(input(f"Solve:\n{number1} * {number2} = "))
    if task2 == number1*number2:
        count+=1
    else: count=0
    task3=float(input(f"Solve:\n{number1} / {number2} = "))
    if task3 == number1/number2:
        count+=1
    else: count=0
    task4=float(input(f"Solve:\n{number1} ^ {number2} = "))
    if task4 == number1 ** number2:
        count+=1
    else: count=0
    
    result=count/5*100
    if result <60:
        print("Grade : 2")
    elif 60<=result<75:
        print("Grade : 3")
    elif 75<=result<=90:
        print("Grade : 4")
    elif result>90:
        print("Grade : 5")
else:
    print("error")
# Choose:


# The program randomly generates examples, taking into account the chosen difficulty level. After the user enters an answer, its correctness is checked.

# Create an exit condition for the loop. (You can initially specify the number of examples)

# At the end of the program, inform the user of their grade:

# <60% - Grade 2 (Hinne 2)
# 60-75% - Grade 3 (Hinne 3)
# 75-90% - Grade 4 (Hinne 4)
# >90% - Grade 5 (Hinne 5)
