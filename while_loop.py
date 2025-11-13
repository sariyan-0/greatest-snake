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
# prime = []
# x = 2

# while x < 1000:
#     c = 0
#     i = 1  
#     while i < x + 1:
#         if x % i == 0:
#             c = c + 1
#         i = i + 1
#     if c == 2:
#         prime.append(x)
#     x = x + 1

# print(prime)
#####################################################
# Q5: Find all perfect numbers under 10000
# perfect = []
# x = 2

# while x < 10000:
#     s = 0
#     i = 1
#     while i < x:
#         if x % i == 0:
#             s = s + i
#         i = i + 1
#     if s == x:
#         perfect.append(x)
#     x = x + 1

# print(perfect)
#####################################################
# Q6: Fibonacci numbers using while
# fib = [0, 1]
# x = 0
# y = 1

# while y < 10000:
#     z = x + y
#     fib.append(z)
#     x = y
#     y = z

# print(fib)

#####################################################
# # Q7: Find the total of all the numbers in a list using the while statemnt
# lst = [10, 50, 40, 5, 20]
# i = 0
# total = 0

# # Keep looping as long as i is less than the number of items in the list
# while i < len(lst): 
#     total = total + lst[i]
#     i = i + 1

# print("Total:", total) 
#####################################################
# Q8: Find the average of the odd numbers in the list

# list = [13, 12, 5, 1, 2]
# c = 0
# total = 0
# x = 0

# while x < len(list):
#     if list[x] % 2 == 0:
#         total = total + list[x]
#         c = c + 1
#     x = x + 1

# av = total / 2
# print(av)
#####################################################
# Q9: print the biggest number in the list
# lst = [12, 18, 3, 100, 65, 25, 7, 15, 90]
# i = 0
# largest = lst[0]

# while i < len(lst):
#     if lst[i] > largest:
#         largest = lst[i]
#     i = i + 1

# print(largest)
#####################################################
# Q10: Organize the following list
lst = [12, 18, 7, 65, 35, 3, 15, 90]
lst2 = []
t = len(lst)
i = 0
while i < t:
    mini = lst[0]
    j = 0
    while j < len(lst):
        if lst[j] < mini:
            mini = lst[j]  
        j = j + 1  
    lst2.append (mini) # Adds mini to lst2
    lst.remove (mini) # Removes mini from lst
    i = i + 1
print(lst2)



# for i in range (t):
#     mini = lst[0]
#     for item in lst:
#         if item < mini:
#             mini = item
#     lst2.append (mini) # Adds mini to lst2
#     lst.remove (mini) # Removes mini from lst

