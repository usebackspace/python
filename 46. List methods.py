print('--------Append Method--------')
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

print()

print('--------extend(iterable) Method--------')
my_list = [1, 2, 3]
my_list1=[4,5,6]
my_list.extend(my_list1)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

print()

print('--------Insert Method--------')
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]

print()

print('--------Remove Method--------')
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2, 4]

print()

print('--------Pop Method--------')
my_list = [1, 2, 3, 4]
popped_item = my_list.pop(1)
print(popped_item)  # Output: 2
print(my_list)
my_list = [1, 2, 3, 4]
popped_item = my_list.pop()
print(popped_item)  # Output: 4
print(my_list)

print()

print('--------Clear Method--------')
my_list = [1, 2, 3, 4, 5]

# Use the clear() method to remove all items from the list
my_list.clear()

print(my_list)  # Output: []

print()

print('--------Slicing Method To Clear A List --------')
my_list = [1, 2, 3, 4, 5]

# Assign an empty list to the original list
my_list[:] = []

print(my_list)  # Output: []

print()

print('--------Index Method--------')
my_list = [1, 2, 3, 4, 5, 6, 2]
index = my_list.index(2)
print(index)  # Output: 1
index = my_list.index(2 , 3, 7) # 3 is starting of index and 7 is end of index i.e 7-1
print(index)  # Output: 1

print()

print('--------count Method--------')
my_list = [1, 2, 3, 2, 4]
count = my_list.count(2)
print(count)  # Output: 2

print()

print('--------Sort Method--------')
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
my_list.sort()
print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]

print()

print('--------Reverse Method--------')
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # Output: [5, 4, 3, 2, 1]

print()

print('--------Copy Method--------')
original_list = [1, 2, 3]
new_list = original_list.copy()
print(new_list)  # Output: [1, 2, 3]
new_list.append(100)
print('Original List After Appending:',original_list)
print('Appended 100 in copied List :',new_list)

print()

print('--------Len Method--------')
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print("The length of the list is:", length)

print()
