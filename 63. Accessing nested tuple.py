# Nested tuple
print('---- Accessing Only Nested tuple in tuple ----- ')
nested_tuple = ( (2, 3, 4), (5, 6))

# Accessing elements using a nested loop
for i in nested_tuple:
    for j in i:
        print(j, end=' ')
    print()  # Print a new line after each inner tuple

print()

#======================================================================================================
print('---- Accessing Nested tuple with different element in the tuple ----- ')
nested_tuple = (1, (2, 3, 4), 'hello', (5, 6), 7)


for i in range(len(nested_tuple)):
    if type(nested_tuple[i]) is tuple:
        if len(nested_tuple[i])>1:
            x=len(nested_tuple[i])
            for j in range(x):
                print(f"Index [{i}] [{j}] :",nested_tuple[i][j])
            
    else:
        print(f"Index [{i}] :",nested_tuple[i])

print()

#====================================================================================================
print('---- Accessing tuple Using While Loop ----')
# Nested tuple
nested_tuple = ((2, 3, 4),(5, 6))


# Using a while loop to access elements in the nested tuple
i = 0
while i < len(nested_tuple):
    j = 0
    while j < len(nested_tuple[i]):
        print(f"Index [{i}] [{j}] :",nested_tuple[i][j], end=' ')
        j += 1
    print()  # Move to the next line for the next inner tuple
    i+= 1

print()

#=================================================================================================
print('---- Accessing tuple With Different Element Using While Loop ----')
# Nested tuple
nested_tuple = (1, (2, 3, 4), 'hello', (5, 6), 7)


# Using a while loop to access elements in the nested tuple
i = 0
while i < len(nested_tuple):
    j = 0
    if type(i) is tuple:
        while j < len(nested_tuple[i]):
            print(f"Index [{i}] [{j}] :",nested_tuple[i][j], end=' ')
            j += 1
        print()  # Move to the next line for the next inner tuple
        i+= 1
    else:
        print(f"Index [{i}] :",nested_tuple[i])
        i+=1