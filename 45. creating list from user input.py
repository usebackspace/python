my_list=[]

n= int(input("Enter the number of elements: "))

for i in range(n):
    my_list.append(input('Enter the Elements: '))

print(my_list)

print()

print('----Accessing list ------')
for i in my_list:
    print(i)