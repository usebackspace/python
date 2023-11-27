print('---- Tuple Count Method ------')

my_tuple = (1, 2, 3, 2, 'a', 'b', 'a')
count_of_2 = my_tuple.count(2)
count_of_a = my_tuple.count('a')

print(count_of_2)  # Output: 2
print(count_of_a)  # Output: 2

print()

#===================================================================================================

print('---- tuple Index Method -----')

my_tuple = (1, 2, 3, 'a', 'b', 'a')
index_of_2 = my_tuple.index(2)
index_of_a = my_tuple.index('a')

print(index_of_2)  # Output: 1
print(index_of_a)  # Output: 3

print()


#====================================================================================================

print('---- More Precise Tuple Index Method -----')

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50, 20, 60)

# Using tuple.index() to find the index of an element
index_of_30 = my_tuple.index(30)
index_of_20 = my_tuple.index(20)

print(f"Index of 30: {index_of_30}")  # Output: Index of 30: 2
print(f"Index of 20: {index_of_20}")  # Output: Index of 20: 1

# Using tuple.index() with start and end parameters
index_of_20_after_index_1 = my_tuple.index(20, 2)  # Start searching from index 2 onward
index_of_20_between_indices_2_and_5 = my_tuple.index(20, 2, 6)  # Search between indices 2 (inclusive) and 6 (exclusive)

print(f"Index of 20 after index 1: {index_of_20_after_index_1}")  # Output: Index of 20 after index 1: 5
print(f"Index of 20 between indices 2 and 5: {index_of_20_between_indices_2_and_5}")

print()

#============================================================================================================

print('--- To Avoid Valueerror in Count And Index Method ----')

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

# Checking the presence of an element using the 'in' operator
element_to_find = 30

if element_to_find in my_tuple:
    # Using count() method
    count_of_element = my_tuple.count(element_to_find)
    print(f"Count of {element_to_find}: {count_of_element}")

    # Using index() method
    index_of_element = my_tuple.index(element_to_find)
    print(f"Index of {element_to_find}: {index_of_element}")
else:
    print(f"{element_to_find} not found in the tuple.")
