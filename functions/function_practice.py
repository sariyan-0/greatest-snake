############################## FUNCTION PRACTICE ##############################
#
# Q1: Find the divisors of a number
def divisor(x):
    z = []
    for item in range(1, x + 1):
        if x % item == 0:           
            z.append(item)
    return z # <return> only works once

a = divisor(12) 
print(a)


