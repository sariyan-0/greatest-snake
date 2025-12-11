################################## Text Processing ##################################
# str_1 = "My name is Mr. Robot and im here to save the world"
#
# ---------------------------------------------------------------
# Operators:  + ( Concatenation)   NO: "-", "/", "*", "**", "//"
#              <    <=  ?   >=
#                   ==      !=
#
# str_1 = "powersof"
# str_2 = "zero"

# z = str_1 + str_2
# print(z)
#
# if str_1 < str_2:       # A < B < C < ..... < Z < a < b < c ..... < z
#     print("PPOOWWEERR")
# ---------------------------------------------------------------
#       0123456
# str_1 = "zero"

# t = len(str_1)              # 7
# print(t)


# first = str_1[0]            # Index
# print(first)
# ---------------------------------------------------------------
# str_1 = "zero"
# g = ""
# for char in str_1:
#     if char == "e":
#         g += "*"
#     else:
#         g += char
# print(g)
###################################################################
# Q1: Show the hidden phone number
#
#       09124447755     >>>     0912---7755
#       09128482241     >>>     0912---2241
#       09123456789     >>>     0912---6789
#
phone = "09124447755"
#
# g = ""
# for i in range(len(phone)):
#     if 4 <= i <= 6:     # indices 4,5,6
#         g = g + "-"
#     else:
#         g = g + phone[i] # 

# print(g)
###################################################################
# Q2: Remove the selected words from the following string
str_1 = "M,y na.me is Mr. Robo@t and im h;ere to s-a-v-e the wo`rld"
#                       ^^^^^                ^^^^
# ["My", "name", "is", "Mr.", .....]
#
str_1 = str_1 + " "
lst_word = []
g = ""
for char in str_1:      # char ~ "M" >> "y" >> " " >> "i" >> "s"
    if char != " ":     #         OK     OK
        g += char       #   g ~ "My"
    else:               #                        OK
        lst_word.append(g)
        g = ""
print(lst_word)
###################################################################
# Q3: Clean the seperated words
# ['My', 'name', 'is', 'Mr.', 'Robot', 'and', 'im', 'here', 'to', 's-a-v-e', 'the', 'world']
# ---------------------------------------------------------------
# for item in lst_word:
#     if item == "save":
#         print("Error: Must be filterd")
lst_clean = []

for word in lst_word:
    g = ""                 # <-- RESET for each word
    for char in word:
        if char != "-" and char != "=" and char != "+" and char != "/" and char != "*" and char != "_" and char != "@" and char != "#" and char != "$" and char != "%" and char != "^" and char != "&" and char != "(" and char != ")" and char != "." and char != "?" and char != ">" and char != "<" and char != "," and char != "!" and char != "?" and char != "'" and char != "[" and char != "]" and char != ";" and char != ":" and char != "~" and char != "`" and char != "|": 
            g += char
    lst_clean.append(g)

print(lst_clean)

###################################################################
# Q4: Convert question 2 to function
###################################################################
# Q5: Convert question 3 to function
