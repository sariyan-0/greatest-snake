############################# PRACTICE #############################
# Q1: perimeter of rectangle
# a = 10
# b = 20
# #
# c = a + b
# d = c * 2
# print (d)
# --------------------------------
# Q2: perimeter of circle
# r = 5
# PI = 3.14
# #
# f = 2 * PI * r
# print(f)
# --------------------------------
# Q3: More geometry (Done)
# Square
# a = 5
# p = a * 4
# print (p)
#-----------------
# Triangle
# b = 2
# h = 5

# a = 0.5 * 2 * 5
# print (a) 
# b = 2
# h = 5

# a = 0.5 * 2 * 5
#-----------------
# Sphere Surface Area
# PI = 3.14
# r = 5

# a = 4 * PI * r**2
# print (a)
#-----------------
# Speed
# d = 10
# t = 2

# s = d / t
# print ("Speed:", s ,"M/S") # We use commas to seperate different values in a print statement
# --------------------------------
# Q4: Add limits (Done)
# a = -1
# if a > 100:
#     print("Invalid Score, the mark is more than 100%!")

# elif a > 80:
#     print("HELLL YAHHH")    # Indentation
#     print("Good Job")
#     print("You are amazing!")
# elif a > 70:
#     print("Woow")

# elif a > 50:
#     print("Try harder next time")

# elif a > -1:
#       print("You have to study all summer")
# elif a > 100:
#     print("Invalid Score, the mark is more than")
# else:
#   print("Invalid Score, you entered a negative mark!")
# --------------------------------
# Q5: Detect odd or even numbers (Done)

# Rule:
# If dividing a number by 2 and multiplying back by 2 gives
# the same number -> it is Even
# Otherwise -> it is Odd
# -------------------------------------------------------
# a = 67
# if (a // 2) * 2 == a:   # This is gonna remove the decimal number so that the answer is accurate. Thats why we use "//"  instead of "/" 
#     print(a, "is even")
# else:
#     print(a, "is odd")
#
# ----- OR -----
# x = 67
# if x % 2 == 0:
#     print("Even Number")

# else:
#     print("Odd Number")
# -------------------------------------------------------
# Q6: Which one is bigger?
# a = 50
# b = 50
# c = 50
# if a > b and a > c:
#     print(a, "is bigger")

# elif b > a and b > c:
#     print(b,"is bigger")

# elif c > a and c > b:
#     print(c,"is bigger")
    
# else:
#     print("they are all the same:", a)
# -------------------------------------------------------
# Q7: apply a 20% discount to the prices
# price = [20, 40, 30, 100]
# for discount in price:
#     final_price = discount - (discount * 0.2) # Applies the discount
#     print(final_price)
# -------------------------------------------------------
# Q8: Find the odd numbers in the list
# list = [13, 12, 5, 1]
# for odd in list:
#     if ( odd // 2) * 2 == odd:   # This is gonna remove the decimal number so that the answer is accurate. Thats why we use "//"  instead of "/" 
#         print(odd, "even")
#     else:
#         print(odd,"odd")
# Q9: Find the odd numbers in the list
# -------------------------------------------------------
# Q10: Find the divisors of the number 12 (Not Done)
# x = 12
# if x % 1 == 0:
#     print(1)

# if x % 2 == 0:
#     print(2)

# if x % 3 == 0:
#     print(3)

# if x % 4 == 0:
#     print(4)

# if x % 5 == 0:
#     print(5)

# if x % 6 == 0:
#     print(6)

# if x % 7 == 0:
#     print(7)

# if x % 8 == 0:
#     print(8)

# if x % 9 == 0:
#     print(9)

# if x % 10 == 0:
#     print(10)

# if x % 11 == 0:
#     print(11)

# if x % 12 == 0:
#     print(12)
# --------------------------- Same thing, but with loop
# x = 12
# for item in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}:
#     if x % item == 0:
#         print(item)
# -------------------------------------------------------
# Q11: Find the smallest number in the list
# lst = [12, 18, 7, 65, 25, 3, 15, 90]

# smallest = lst[0]
# for num in lst:
#     if num < smallest:
#         smallest = num

# print(smallest)
# -------------------------------------------------------
# Q12: add a 20% discount for the prices above 10000 tomans
# lst = [10000, 50000, 8000, 90000, 2000, 65000, 40000]

# for price in lst:
#     if price > 10000:
#         final_price = price - (price * 0.2)  # Applies 20% discount if above 10000 toman
#         print(final_price)
#     else:
#         print(price, "(not discounted!)")  # No discount applied
# -------------------------------------------------------
# Q13: Using Range
x = 1200
for item in range(1,x+1): # By using +1 you also include the number itself
    if x % item == 0:
        print(item)
# -------------------------------------------------------
