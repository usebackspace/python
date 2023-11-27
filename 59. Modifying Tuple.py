print('---- Creating a New Tuple -----')
# Original tuple
my_tuple = (1, 2, 3, 4, 5)

# Creating a new tuple with modifications
modified_tuple = my_tuple[:2] + (6, 7) + my_tuple[3:]

print(modified_tuple)  # Output: (1, 2, 6, 7, 4, 5)

print()

#==========================================================================================================

print('----- Converting to List and then Back to tuple ------')
# Original tuple
my_tuple = (1, 2, 3, 4, 5)

# Converting tuple to list
tuple_list = list(my_tuple)

# Modifying the list
tuple_list[2] = 6
tuple_list[3] = 7

# Converting list back to tuple
modified_tuple = tuple(tuple_list)

print(modified_tuple)  # Output: (1, 2, 6, 7, 5)

print()

#================================================================================================
print('----- Using "namedtuple" from "collection" module ------')
from collections import namedtuple

# Syntax:
# TypeName = namedtuple('TypeName', ['field1', 'field2', ...])

# Creating a named tuple
MyTuple = namedtuple('MyTuple', ['a', 'b', 'c', 'd', 'e'])
my_tuple = MyTuple(1, 2, 3, 4, 5)

# Creating a new named tuple with modifications
modified_tuple = my_tuple._replace(c=6, d=7)

print(modified_tuple)  # Output: MyTuple(a=1, b=2, c=6, d=7, e=5)
