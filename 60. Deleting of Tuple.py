print('----- Deleting Tuple Using Slicing Method')
# Original tuple
my_tuple = (1, 2, 3, 4, 5)

# Creating a new tuple without the element 3
new_tuple = my_tuple[:2] + my_tuple[3:]

print(new_tuple)  # Output: (1, 2, 4, 5)

print()

#=======================================================================================================

print('----- Deleting Tuple by converting to the list then again back to the tuple ----')

# Original tuple
my_tuple = (1, 2, 3, 4, 5)

# Converting tuple to list
tuple_list = list(my_tuple)

# Removing an element
tuple_list.remove(3)

# Converting list back to tuple
new_tuple = tuple(tuple_list)

print(new_tuple)  # Output: (1, 2, 4, 5)
