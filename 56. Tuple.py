# Creating an empty tuple
print('---- Creating a empty tuple ----')
empty_tuple = ()

print()
#====================================================================================================

print('----- Creating a tuple with different element ------')
# Creating a tuple with elements
my_tuple = (1, 2, 3, 'a', 'b')

print()

#====================================================================================================

print('----- Accessing Tuple ------')
first_element = my_tuple[0]
print(first_element)  # Output: 1

print()

#====================================================================================================
print('----- Slicing of Tuple -------')

subset_of_tuple = my_tuple[1:3]
print(subset_of_tuple)  # Output: (2, 3)

print()

#=================================================================================================
print('---- Immutable Nature ------')
# This will raise an error
# my_tuple[0] = 100

print()

#=================================================================================================

print('----- Mixed Tuple ------')

mixed_tuple = (1, 'two', 3.0, [4, 5])
print(mixed_tuple)

print()

#=================================================================================================

print('---- Length of Tuple -----')
tuple_length = len(my_tuple)
print(tuple_length)  # Output: 5

print()

#===================================================================================================

print('---- Nested Tuple ------')
nested_tuple = (1, (2, 3), ('a', 'b'))

print()

#=====================================================================================================
print('----- Unpacking of Tuple -----')
my_tuple = (1, 2, 3, 'a', 'b')
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 'a' 'b'

print()

#=======================================================================================================
print('---- Contatenation Of Tuple -----')
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')

print()

#=========================================================================================================

print('----- Repetition Operator -----')
repeated_tuple = my_tuple * 2
print(repeated_tuple)  # Output: (1, 2, 3, 'a', 'b', 1, 2, 3, 'a', 'b')

print()

#==========================================================================================================

print('------ Using Membership Operator ------')
print(2 in my_tuple)  # Output: True
print('x' in my_tuple)  # Output: False


