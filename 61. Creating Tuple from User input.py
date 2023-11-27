my_tuple=[]

n= int(input("Enter the number of elements: "))

for i in range(n):
    my_tuple.append(input('Enter the Elements: '))

print()

print('---- After Appending tuple is ----')
print("Before converting into tuple :",my_tuple)

print()

my_tuple=tuple(my_tuple)

print(my_tuple)

print()

print('----Accessing tuple ------')
for i in my_tuple:
    print(i)