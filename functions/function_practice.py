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
a = average(    [12, 18, 7, 65, 35, 3, 15, 4 ]  )
print(a)
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
lst_50 = [12, 18, 7, 65, 35, 3, 15, 4 ]
a = sorting(lst_50)
print (a)