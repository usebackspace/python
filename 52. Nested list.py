nested_list = [1, [2, 3, 4], 'hello', [5, 6], 7]

print('----  Result of Unmodified Nested List ------')
# Accessing elements in the nested list
print("0 Index :",nested_list[0])          # Output: 1
print("1 Index :",nested_list[1])          # Output: [2, 3, 4]
print("[1][0] Index :",nested_list[1][0])       # Output: 2 (accessing an element within the inner list)
print("2 Index :",nested_list[2])          # Output: 'hello'

print()

print('----  Result of Modified Nested List ------')
# Original nested list
nested_list = [1, [2, 3, 4], 'hello', [5, 6], 7]

# Modify an element within an inner list
nested_list[1][0] = 'X'

# Add a new element to an inner list
nested_list[3].append(7)

# Replace an entire inner list
nested_list[2] = [8, 9, 10]

# Add 8 to the last element
nested_list.append(8)

# Display the modified nested list
print(nested_list)
