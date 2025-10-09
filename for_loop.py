############################# FOR LOOP #############################
# Loops are made to repeat a specific action or command
#
# 
for list in [5, 2, 5, 3]: # "100" X wrong!          
    z = list + 100 # Each are embedded one by one 
    print(z)

# A better and cleaner way
list = [5, 2, 5, 3]
for number in list: # "100" X wrong!          
    z = number + 100 # Each are embedded one by one 
    print(z)

# Using Range
x = 1200
for item in range(1,x+1): # By using +1 you also include the number itself
    if x % item == 0:
        print(item)
