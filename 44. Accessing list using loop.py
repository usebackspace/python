my_list = [1, 2, 3, 4, 5]

# Using a for loop to access and print each element
print('--- Acessing list using for loop ------')
for item in my_list:
    print(item)

print()

print('--- Acessing list using range function in for loop ------')
for i in range(len(my_list)):
    print(i,my_list[i])

print()

print('--- Acessing list using while loop ------')
my_list = [1, 2, 3, 4, 5]
index = 0  # Start at the first element

# Using a while loop to access and print each element
while index < len(my_list):
    print(my_list[index])
    index += 1
