############################## FUNCTION PRACTICE ##############################
#
# Q1: Find the divisors of a number
def divisor(x):
    z = []
    for item in range(1, x + 1):
        if x % item == 0:           
            z.append(item)
    return z # <return> only works once

# Call
# a = divisor(12) 
# print(a)
############################################################
# Q2: Detect if x is a prime or not

def is_prime(x):  
    c = 0
    for item in range(1, x + 1):
        if x % item == 0:
            c = c + 1  
    if c == 2:
        return "A prime number"
    else:
        return "Not a prime number"

# Call       
# a = is_prime(13)
# print(a)
############################################################
# Q3: Find the smallest number in the list
def minimun(lst_x):
    mini = lst_x[0]
    for item in lst_x:
        if item < mini:
            mini = item
    return mini

# Call
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

# Call
a = maximum(    [12, 18, 7, 65, 35, 3, 15, 4 ]  )
print (a) # 3