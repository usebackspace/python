# Creating a tuple of list
tuple_of_list = (
    [1, 'apple'],
    [2, 'banana'],
    [3, 'cherry'],
    [4, 'date'],
    5, 6,7
)

print('---- Accessing tuple of list using Index----')
# Accessing elements in the tuple of list
print(tuple_of_list[0])  # Output: (1, 'apple')
print(tuple_of_list[1][1])  # Output: 'banana'

print()

#=============================================================================================================
print('---- Accessing tuple of list using For loop----')

# Iterating over the tuple of list
for item in tuple_of_list:
    print(item)

print()

#==========================================================================================================
print('---- Modifiying list ----')
# Modifying the tuple of list
# tuple_of_list[0] = [5, 'elderberry']
# tuple_of_list.append([6, 'fig'])

print(tuple_of_list)

print()

#===============================================================================================================
print('---- Deleting list ----')
# del tuple_of_list[1]
print(tuple_of_list)

# del tuple_of_list
print(tuple_of_list)