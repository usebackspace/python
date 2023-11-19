# Nested list
print('---- Accessing Only Nested list in List ----- ')
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements using a nested loop
for i in nested_list:
    for j in i:
        print(j, end=' ')
    print()  # Print a new line after each inner list

print()

#======================================================================================================
print('---- Accessing Nested list with different element in the List ----- ')
nested_list = [1, [2, 3, 4], 'hello', [5, 6], 7]

for i in range(len(nested_list)):
    if type(nested_list[i]) is list:
        if len(nested_list[i])>1:
            x=len(nested_list[i])
            for j in range(x):
                print(f"Index [{i}] [{j}] :",nested_list[i][j])
            
    else:
        print(f"Index [{i}] :",nested_list[i])

print()

#====================================================================================================
print('---- Accessing List Using While Loop ----')
# Nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using a while loop to access elements in the nested list
i = 0
while i < len(nested_list):
    j = 0
    while j < len(nested_list[i]):
        print(f"Index [{i}] [{j}] :",nested_list[i][j], end=' ')
        j += 1
    print()  # Move to the next line for the next inner list
    i+= 1

print()

#=================================================================================================
print('---- Accessing List With Different Element Using While Loop ----')
# Nested list
nested_list = [1, [2, 3, 4], 'hello', [5, 6], 7]

# Using a while loop to access elements in the nested list
i = 0
while i < len(nested_list):
    j = 0
    if type(i) is list:
        while j < len(nested_list[i]):
            print(f"Index [{i}] [{j}] :",nested_list[i][j], end=' ')
            j += 1
        print()  # Move to the next line for the next inner list
        i+= 1
    else:
        print(f"Index [{i}] :",nested_list[i])
        i+=1