print('------- Concatenating With + Operator ------')
list1 = [1, 2, 3]
list2 = [4, 5, 6]

concatenated_list = list1 + list2
print(concatenated_list)

print()

#=====================================================================

print('------ Concatenating With extend() method -------')
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)
