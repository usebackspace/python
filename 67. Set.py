print('---- Syntax ----')
set1 = {1, 2, 3,'hello',6}

set2 = set([3, 4, 5,'hello',6])  # using Set() constructor
 
print(set1)
print(set2)

print()

#============================================================================================================

print('----Using set() with the * unpacking operator----')
# Sytnax
# empty_set = set(*[])

# Method Not Recommended 
elements = [1, 2, 3, 4, 5]

# Using set() with the * unpacking operator
my_set = set(*[elements])

print(my_set)

print()

#============================================================================================================

print('---- Creating an Empty set ----')
empty_set = set()
print(empty_set)

print()

#==============================================================================================================

print('---- Uniqueness of set ----')
unique_set = {1, 2, 3, 3, 4, 2, 4}
print(unique_set)  # Output: {1, 2, 3, 4}

print()

#==============================================================================================================

print('---- Unorder properties of set -----')
my_set = {4, 2, 1, 3}
print(my_set)  # Output: {1, 2, 3, 4}

print()

#==============================================================================================================

print('---- Mutable properties of set ----')

my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

print()

#==============================================================================================================

print('---- Membership Operator in set ----')

my_set = {1, 2, 3, 4, 5}
print(2 in my_set)  # Output: True

print()

#==============================================================================================================

print('---- Accessing Set using for loop ----')

set1 = {1, 2, 3,'hello',6}
for i in set1:
    print(i)

print()