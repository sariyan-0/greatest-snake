############################## FUNCTION PRACTICE ##############################
#
# Q1: Find the divisors of a number
# def

def divisor(x):
    z = []
    for item in range(1, x + 1):
        if x % item == 0:           
            z.append(item)
    return z # <return> only works once

# call
# a = divisor(12) 
# print(a)
############################################################
# Q2: Detect if x is a prime or not
# def

def is_prime(x):  
    c = 0
    for item in range(1, x + 1):
        if x % item == 0:
            c = c + 1  
    if c == 2:
        return "A prime number"
    else:
        return "Not a prime number"

# call     
# a = is_prime(13)
# print(a)
############################################################
# Q3: Find the smallest number in the list
# def
def minimun(lst_x):
    mini = lst_x[0]
    for item in lst_x:
        if item < mini:
            mini = item
    return mini

# call
# a = minimun(    [12, 18, 7, 65, 35, 3, 15, 4 ]  )
# print (a) # 3
############################################################
# Q4: Find the biggest number in the list
def maximum(lst_x):
    maxi = lst_x[0]
    for item in lst_x:
        if item > maxi:
            maxi = item
    return maxi

# call
# a = maximum(    [12, 18, 7, 65, 35, 3, 15, 4 ]  )
# print (a) # 3
############################################################
# Q5: Total sum of the numbers in a list
# def
def sum_lst(lst_x):
    g = 0
    for item in lst_x:
        g = g + item
    return g

# call
# a = sum_lst(    [12, 18, 7, 65, 35, 3, 15, 4 ]  )
# print(a)
############################################################
# Q5: Total average of a list
# def
def average(lst_x):
    t = len (lst_x)
    total = 0
    for item in lst_x:
        total = total + item

    avg = total / t
    return avg

# call
# a = average(    [12, 18, 7, 65, 35, 3, 15, 4 ]  )
# print(a)
############################################################
# Q6: Orgenize the list
# def

lst = [12, 18, 7, 65, 35, 3, 15, 4 ]
def sorting(lst_x):
    lst_2 = []
    t = len(lst_x)
    for i in range(t):
        mini = lst_x[0]
        for item in lst_x:
            if item < mini:
                mini = item
        
        lst_2.append(mini)
        lst_x.remove(mini)
    return(lst_2)

# call
# lst = [12, 18, 7, 65, 35, 3, 15, 4 ]
# a = sorting(lst)
# print (a)
############################################################
# Q7: Find the common numbers in both lists
# def

def common_items(lst_x, lst_y):
    lst_common = []
    for item_a in lst_x:
        if item_a in lst_y:
            lst_common.append(item_a)
    return lst_common


# call
lst_1 = [12, 18, 7, 65, 35, 3, 15, 90]
lst_2 = [90, 13, 12, 15, 16, 8, 2, 11]

# a = common_items(lst_1, lst_2)
# print(a)
############################################################
# Q8: Find all the prime numbers under 1000
# Ex: 2, 3, 5, 7, 11, 13, ...., 997
# define
def primes():
    prime_lst = []
    for x in range(1, 1000):
        c = 0
        for i in range(1, x + 1):
            if x % i == 0:
                c = c + 1
        if c == 2:
            prime_lst.append(x)
    return prime_lst

# call
# a = primes()
# print(a)
############################################################
# Q9: Find if x is in the list or not?

x = 7
# Yes/No
# define
def exist(number_x, lst_x): # Two inputs, one for finding the number and the other for the list
    label = "No"
    for item in lst:
        if x == item:
            label = "Yes"


    if label == "Yes":
        return "Yes, we found the number!"

    else:
        return "No, we didnt find the number!"
    
# call
# lst_x = [12, 18, 7, 65, 35, 5, 15, 90]
# a  = exist(12, lst_x)
# print(a)
############################################################
# Q10: Find the repeted numbers in the lists
# define
lst_x = [12, 18, 7, 65, 35, 12, 15, 90, 7, 65, 4]

def repeated(numbers):
    repeated_items = []
    for num in numbers:
        c = lst_x.count(num)
        if c > 1 and num not in repeated_items:
            repeated_items.append(num)
    return repeated_items

# call
# a = repeated(lst_x)
# print(a)
############################################################
# Q11: Find the average of 3 digit prime numbers

lst_p = []
for num in range(100, 1000):
    a =  is_prime(num)
    if a == "A prime number":
        lst_p.append(num)
av = average(lst_p)
print(av)           #524.94
############################################################
# ----------------------------------------------------------
# Q12: Largest common multiple
#
# 12 >>> 1, 2, 3, 4, 6, 8
#                           >>> 1, 2, 3, 6, >>> 6
# 18 >>> 1, 2, 3, 6, 9, 18
# ----------------------------------------------------------
#
#           <<<< Functions are Reusable >>>>
#
# ----------------------------------------------------------
# Biggest common number
# lst_12 = divisor(12)
# lst_18 = divisor(18)
# lst_c = common_items(lst_12, lst_18)
# lcm = maximum(lst_c)
# print(lcm)
# ----------------------------------------------------------
# x = 12
# lst_12 = []
# for item in range (1, x + 1):
#     if x % item == 0:
#         lst_12.append(item)

# # print(lst_12)
# y = 18
# lst_18 = []
# for item in range(1, y + 1):
#     if y % item == 0:
#         lst_18.append(item)
# # print(lst_18)
# lst_c = []
# for a in lst_12:
#     for b in lst_18:
#         if a == b:
#             lst_c.append(b)
# # print(lst_c)

# def maximum(lst_x):
#     maxi = lst_x[0]
#     for item in lst_x:
#         if item > maxi:
#             maxi = item
#     return maxi

# # call
# a = maximum(lst_c)
# print (a) # 6

############################################################
# Q13: 
############################################################
# Q14: 
############################################################
# Q15: 
############################################################
# Q16: 