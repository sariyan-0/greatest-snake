def divisor(x):
    z = []
    for item in range(1, x + 1):
        if x % item == 0:           
            z.append(item)
    return z # <return> only works once


def is_prime(x):  
    c = 0
    for item in range(1, x + 1):
        if x % item == 0:
            c = c + 1  
    if c == 2:
        return "A prime number"
    else:
        return "Not a prime number"

   
def minimun(lst_x):
    mini = lst_x[0]
    for item in lst_x:
        if item < mini:
            mini = item
    return mini


def maximum(lst_x):
    maxi = lst_x[0]
    for item in lst_x:
        if item > maxi:
            maxi = item
    return maxi


def sum_lst(lst_x):
    g = 0
    for item in lst_x:
        g = g + item
    return g


def average(lst_x):
    t = len (lst_x)
    total = 0
    for item in lst_x:
        total = total + item

    avg = total / t
    return avg


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


def common_items(lst_x, lst_y):
    lst_common = []
    for item_a in lst_x:
        if item_a in lst_y:
            lst_common.append(item_a)
    return lst_common


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


def repeated(x):
    repeated_items = []
    for num in x:
        c = x.count(num)
        if c > 1 and num not in repeated_items:
            repeated_items.append(num)
    return repeated_items


def exist(number_x, lst_x): # Two inputs, one for finding the number and the other for the list
    label = "No"
    for item in lst_x:
        if number_x == item:
            label = "Yes"


    if label == "Yes":
        return "Yes, we found the number!"

    else:
        return "No, we didnt find the number!"
    
def corrected_words(lst_word):
    lst_correct = []

    for word in lst_word:
        g = ""
        for char in word:
            if char not in "~!@#$%^&*()_+=-|\}]{[]}:;'.,><":
                g += char
        lst_correct.append(g)

    return lst_correct

def clean_words(lst_word):
    lst_clean = []

    for word in lst_word:
        g = ""
        for char in word:
            if char != "-" and char != "=" and char != "+" and char != "/" and char != "*" and char != "_" and char != "@" and char != "#" and char != "$" and char != "%" and char != "^" and char != "&" and char != "(" and char != ")" and char != "." and char != "?" and char != ">" and char != "<" and char != "," and char != "!" and char != "?" and char != "'" and char != "[" and char != "]" and char != ";" and char != ":" and char != "~" and char != "`" and char != "|":
                g += char
        lst_clean.append(g)

    return lst_clean