nested_tuple = (1, (2, 3, 4), 'hello', (5, 6), 7)

print('----  Result of Unmodified Nested tuple ------')
# Accessing elements in the nested tuple
print("0 Index :",nested_tuple[0])          # Output: 1
print("1 Index :",nested_tuple[1])          # Output: [2, 3, 4]
print("[1][0] Index :",nested_tuple[1][0])       # Output: 2 (accessing an element within the inner tuple)
print("2 Index :",nested_tuple[2])          # Output: 'hello'

print()

