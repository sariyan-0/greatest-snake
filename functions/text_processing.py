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
str_1 = "zero"
g = ""
for char in str_1:
    if char == "e":
        g += "*"
    else:
        g += char
print(g)