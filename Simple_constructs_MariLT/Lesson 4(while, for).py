#Task 1
#Input 15 numbers. Determine how many of them are integers.

for i in range(1,16):
    
    number=float(input("Enter number "))
    
    if number.is_integer():
       print(f"Integer {number}")
       integer_count=0
       integer_count+=i    
    print(integer_count)
print()



# #Task 2
# #Ask the user for a number 𝐴  and find the sum of all natural numbers from 1 to 𝐴.

# while True:
#     try:
#         A=int(input("Enter an integer number "))
#         break
#     except:

#         print("Number has to be integer.")
# summ=0
# if A>0:
#     for i in range(1, A+1):
#         summ+=i
#         print(f"i step {summ}")
#     print(f"\nAnswer {summ}")

# #Task 3
# #Input 8 numbers. Find the product of the positive numbers only.
# p=1
# for j in range (8):
#     while True:
#         try:
#             num=float(input(f"Enter a number {j+1} "))
#             break
#         except:

#             print("Insert number.") 
#     if num>0: p*num
#     print(f"{j+1}. step of a product is {p}")
# print(f" Final result is {p}")

# #Task 4

# for i in range(10, 21): print(i**2, end=",")

# print("\n\n")

#Task 5
#Create a program that calculates the sum of only the negative numbers from N numbers. 
#The value of N is entered from the keyboard.



# #Task 15

# for j in range(10):
#     for i in range(10):
#         print(i, end=" ")
#     print()          
# print() 

# #Task 16
# for j in range(1,10):
#     for i in range(1,10):
#         if i==j:
#             print(j, end=" ")
#         else:
#             print("0", end=" ")
#     print()

   