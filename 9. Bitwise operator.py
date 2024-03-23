# Bitwise AND (&)
x = 12  # Binary: 0101
y = 9 # Binary: 0011
result_and = x & y
print("Bitwise AND:", result_and)  # Result: 0001 (1 in decimal)

# Bitwise OR (|)
result_or = x | y
print("Bitwise OR:", result_or)  # Result: 0111 (7 in decimal)

# Bitwise XOR (^)
result_xor = x ^ y
print("Bitwise XOR:", result_xor)  # Result: 0110 (6 in decimal)

# Bitwise NOT (~)
x = 5  # Binary: 0101
result_not_x = ~x
print("Bitwise NOT:", result_not_x)  # Result: 11111010 (-6 in decimal)

# Left Shift (<<)
x = 12  # Binary: 0101
result_left_shift = x << 2
print("Left Shift:", result_left_shift)  # Result: 010100 (20 in decimal)

# Right Shift (>>)
x = 12  # Binary: 010100
result_right_shift = x >> 2
print("Right Shift:", result_right_shift)  # Result: 0101 (5 in decimal)
