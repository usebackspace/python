print('---------- Adding 2 number and checking there datatype -----------')
x = 5  # int
y = 2.5  # float
result = x + y  # Implicitly converts x to float and then performs addition
print(result)  # Output: 7.5
print(type(result))

print()

print('-------- Explicitly Converting Into Float ----------')
x = 5.7  # float
y = int(x)  # Explicitly converts x to an integer
print(y)  # Output: 5
print(type(y))

print()

print('--------- Explicitly Converting String Datatype Into Integer ---------')
num = "42"  # str
print(num)
print(type(num))
x = int(num)  # Explicitly converts num_str to an integer
print(x)  # Output: 42
print(type(x))

print()

value = 3  # int
float_value = float(value)  # Explicitly converts value to a float
print(float_value)  # Output: 3.0
print(type(float_value))
