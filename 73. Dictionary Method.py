print('-----1. Clear Method -----')

my_dict = {'a': 1, 'b': 2, 'c': 3}

print("Original Dictionary:", my_dict)

my_dict.clear()

print("Dictionary after clear():", my_dict)

print()

#==========================================================================================================
print('-------- copy() Method --------')
print('-----2. Shallow Copy -----')
original_dict = {'a': 1, 'b': [2, 3], 'c': {'x': 4, 'y': 5}}

copied_dict = original_dict.copy()

original_dict['b'][0] = 99
original_dict['a'] = 100


print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)

print()

#==========================================================================================================

print('----2.1 Deep Copy Method ----')

import copy

original_dict = {'a': 1, 'b': [2, 3], 'c': {'x': 4, 'y': 5}}

deep_copied_dict = copy.deepcopy(original_dict)

original_dict['b'][0] = 99
original_dict['a'] = 100


print("Original Dictionary:", original_dict)
print("Deep Copied Dictionary:", deep_copied_dict)

print()

#==========================================================================================================

print('---- fromkeys() method ----')

print()

keys = ['a', 'b', 'c']
default_value = 100
print(' -- With Single Value--')
my_dict = dict.fromkeys(keys, default_value)
print(my_dict)

print()

print(' -- With Mutliple Value--')
default_value = (100,200)
my_dict = dict.fromkeys(keys, default_value)
print(my_dict)

print()

keys = ['x', 'y', 'z']
print(' -- Default Value Is Not Given --')
my_dict = dict.fromkeys(keys)
print(my_dict)

print()

#==========================================================================================================

print('----- get() method -----')
# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# value_x=my_dict['d']
value_a = my_dict.get('a')
value_d = my_dict.get('d')  # Key 'd' is not present

# Specifying a default value
value_e = my_dict.get('e', 0)  # Key 'e' is not present, default value is 0

# Print the results
print("Value for 'a':", value_a)  
print("Value for 'd':", value_d)  
print("Value for 'e':", value_e)  

print()

#==========================================================================================================

print('---- items() Method -----')

my_dict = {'a': 1, 'b': 2, 'c': 3}
# Using items() to get key-value pairs
items = my_dict.items()

print(items)

print('---- Accessing Key-Value through for loop ----')

my_dict = {'a': 100, 'b': 200, 'c': 300}

for key, value in my_dict.items():
    print(f"Key: {key}   Value: {value}")

print()

#==========================================================================================================

print('---- key() method ----')
# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

keys_view = my_dict.keys()

print("Original Dictionary:", my_dict)
print("Keys View:", keys_view)

print()

#==========================================================================================================

print('---- values() method ----')
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# Using values() method to get a view of values
values_view = my_dict.values()

# Displaying the result
print("Original Dictionary:", my_dict)
print("Values View:", values_view)

print()

#==========================================================================================================

print('----- Pop() Method ----')

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using pop without default value
value = my_dict.pop('b')
print(f"Removed value: {value}")  # Output: Removed value: 2
print(f"Modified dictionary: {my_dict}")  # Output: Modified dictionary: {'a': 1, 'c': 3}

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using pop with default value
value = my_dict.pop('x', 0)
print(f"Removed value: {value}")  # Output: Removed value: 0
print(f"Modified dictionary: {my_dict}")  # Output: Modified dictionary: {'a': 1, 'c': 3}

print()

#==========================================================================================================

print('---- Popitem() Method ----')
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using popitem() to remove and return the last item
removed_item = my_dict.popitem()

print("Removed item:", removed_item)
print("Updated dictionary:", my_dict)

print()

#==========================================================================================================

print('----- Setdefault() method -----')
my_dict = {'a': 1, 'b': 2, 'c': 3}

print('--setdefault for an existing key--')
value_a = my_dict.setdefault('a', 100)
print(value_a)  # Output: 1 (existing value for key 'a')
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

print()

print('--setdefault for a new key--')
value_d = my_dict.setdefault('d',100)
print(value_d)  # Output: 0 (default value for key 'd')
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 0}


print()

#==========================================================================================================

print('----- Update() method -----')

dict1 = {'a': 1, 'b': 2}

dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)

dict1.update({'d':'5'})

print(dict1)

print()

#==========================================================================================================
