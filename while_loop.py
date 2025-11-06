#################### While Loop ####################
# x = 12
# for item in range(1, x +1 ):
#     if x % item == 0:
#         print(item)
# --------------------------------------------------
# x = 12
# i = 1                   # Part 1: Definition of the variable
# while i < x + 1:        # Part 2: Loop rule
#     if x % item == 0:
#         print(i)
#     i = i + 1           # Part 3: Taking a step forward
#####################################################
# x = 103
# c = 0
# i = 1
# while i < x + 1:
#     if x % i == 0:
#         c = c + 1
#     i = i + 1
# #
# if c == 2:
#     print("This is a prime number")
# else:
#     print("This is NOT a prime number")
#####################################################
# Q2: Detect perfect  numbers using while

# x = 6
# total = 0
# i = 1
# while i < x:
#     if x % i == 0:
#         total = total + i
#     i = i + 1
# if total == x:
#     print("This is a perfet number")
# else:
#     print("This is not a perfect number")
#####################################################
# Q3: Find the multiples of 7 that are 3 digits
# i = 1
# total = 0
# while i < 1000:
#     if i % 7 == 0:
#         total = total + 1
#     i = i + 1
# print (total)
#####################################################
# Q4: Find prime numbers under 1000
prime = []
x = 2

while x < 1000:
    c = 0
    i = 1  
    while i < x + 1:
        if x % i == 0:
            c = c + 1
        i = i + 1
    if c == 2:
        prime.append(x)
    x = x + 1

print(prime)
#####################################################
# Q5: Find all perfect numbers under 10000

#####################################################
# Q6: Fibonacci numbers using while

#####################################################
# Q7: Find the total of all the numbers in a list using the while statemnt
lst = [10, 50, 40, 5, 20]
