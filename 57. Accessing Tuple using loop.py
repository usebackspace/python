my_tuple = (1, 2, 3, 4, 5)

# Using a for loop to access and print each element
print('--- Acessing tuple using for loop ------')
for item in my_tuple:
    print(item)

print()

print('--- Acessing tuple using range function in for loop ------')
for i in range(len(my_tuple)):
    print(i,my_tuple[i])

print()

print('--- Acessing tuple using while loop ------')
my_tuple = (1, 2, 3, 4, 5)
index = 0  # Start at the first element

# Using a while loop to access and print each element
while index < len(my_tuple):
    print(my_tuple[index])
    index += 1
