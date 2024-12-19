#Write a program for testing mathematical knowledge.
import random
import operator
# Offer the user to choose the difficulty level of the tasks. For example:
level=input("Choose complexity level(1,2,3): ")
# The number of operations (+, -, /, *, **)

# The range of randomly generated numbers.

count=0
tasks_number=0
#use .split() or .split(',') first if parse by space second if by ,
operators = ['+', '-', '*', '/', '**']
operations = { '+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '**': operator.pow }

# Level 1 (Tase 1)
if level == "1":
    tasks_total=10
    while tasks_number != tasks_total:
        chosen_operator = random.choice(operators)
        number0=random.randint(1, 10)
        number1=random.randint(1, 10)
        # if chosen_operator == '**' and number0 > 5: number1 = random.randint(1, 5)
        if chosen_operator == '**' and number1 > 5: number1 = random.randint(1, 5)
        op_result = operations[chosen_operator](number0, number1)
        task0=float(input(f"Solve:\n{number0} {chosen_operator} {number1} = "))
        if task0 == op_result:
            print("Correct!")
            count+=1
        else: 
            count=0
            print(f"Incorrect. The correct answer is {op_result}")
        tasks_number+=1
        
    
    

# Level 2 (Tase 2)

if level == "2":
    tasks_total=20
    while tasks_number != tasks_total:
        chosen_operator0 = random.choice(operators)
        chosen_operator1 = random.choice(operators)
        number0=random.randint(1, 100)
        number1=random.randint(1, 100)
        number2=random.randint(1, 100)
        if chosen_operator0 == '**' and number1 > 5: number1 = random.randint(1, 5)
        if chosen_operator1 == '**' and number1 > 5: number2 = random.randint(1, 5)
        
        op_result = operations[chosen_operator0](number0, number1)
        op_result = operations[chosen_operator1](op_result, number2)
        task0=float(input(f"Solve:\n{number0} {chosen_operator0} {number1} {chosen_operator1} {number2}= "))
        if task0 == op_result:
             print("Correct!")
             count+=1
        else: 
            count=0
            print(f"Incorrect. The correct answer is {op_result}")
        tasks_number+=1

    
# Level 3 (Tase 3)

if level == "3":
    tasks_total=30
    while tasks_number != tasks_total:
        chosen_operator0 = random.choice(operators)
        chosen_operator1 = random.choice(operators)
        chosen_operator2 = random.choice(operators)
        number0=random.randint(1, 100)
        number1=random.randint(1, 100)
        number2=random.randint(1, 100)
        number3=random.randint(1, 100)
        if chosen_operator0 == '**' and number1 > 5: number1 = random.randint(1, 5)
        if chosen_operator1 == '**' and number1 > 5: number2 = random.randint(1, 5)
        if chosen_operator2 == '**' and number1 > 5: number3 = random.randint(1, 5)
        op_result = operations[chosen_operator0](number0, number1)
        op_result = operations[chosen_operator1](op_result, number2)
        op_result = operations[chosen_operator2](op_result, number3)
        task0=float(input(f"Solve:\n{number0} {chosen_operator0} {number1} {chosen_operator1} {number2} {chosen_operator1} {number2}= "))
        if task0 == op_result:
             print("Correct!")
             count+=1
        else: 
            count=0
            print(f"Incorrect. The correct answer is {op_result}")
        tasks_number+=1
 
result=count/tasks_number*100
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

