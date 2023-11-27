my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Get elements from index 2 to 5 (exclusive)
result = my_tuple[2:5]
print(result)  # Output: [2, 3, 4]

# Get every second element from index 1 to 8
result = my_tuple[1:8:2]
print(result)  # Output: [1, 3, 5, 7]

# Get all elements from index 5 to the end
result = my_tuple[5:]
print(result)  # Output: [5, 6, 7, 8, 9]

# Get all elements from the beginning to index 3 (exclusive)
result = my_tuple[:3]
print(result)  # Output: [0, 1, 2]

# Get a copy of the entire tuple
result = my_tuple[:]
print(result)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
