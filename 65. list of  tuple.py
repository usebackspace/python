# Creating a list of tuples
list_of_tuples = [
    (1, 'apple'),
    (2, 'banana'),
    (3, 'cherry'),
    (4, 'date'),
    5, 6,7
]

print('---- Accessing list of tuple using Index----')
# Accessing elements in the list of tuples
print(list_of_tuples[0])  # Output: (1, 'apple')
print(list_of_tuples[1][1])  # Output: 'banana'

print()

#=============================================================================================================
print('---- Accessing list of tuple using For loop----')

# Iterating over the list of tuples
for item in list_of_tuples:
    print(item)

print()

#==========================================================================================================
print('---- Modifiying list ----')
# Modifying the list of tuples
list_of_tuples[0] = (5, 'elderberry')
list_of_tuples.append((6, 'fig'))

print(list_of_tuples)

print()

#===============================================================================================================
print('---- Deleting list ----')
del list_of_tuples[1]
print(list_of_tuples)

# del list_of_tuples
print(list_of_tuples)