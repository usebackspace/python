print('------ Creating an Empty list-------')
x=[]
print(x)

print()

print('--------Creating a list -----------')
my_list = [1, 2, 3, 4, 5]  # A list of integers
words = ["apple", "banana", "cherry"]  # A list of strings
mixed_list = [1, "two", 3.0, True]  # A list with mixed data types

print('Output of my_list:',my_list)
print('output of word:',words)
print('output of mixed_list:',mixed_list)

print()

print('------ Accessing List -------')
my_list = [1, 2, 3, 4, 5]
print('Accessing list at index 0 :',my_list[0])  # Access the first element (1)
print('Accessing list at index 1 :',my_list[1])  # Access the second element (2)
print('Accessing list at index -1 :',my_list[-1])  # Access the last element (5) using negative indexing

print()

print('----- Modifying list ---------')
my_list = [1, 2, 3, 4, 5]
print('List before modifying:',my_list)
my_list[2] = 6  # Modify the third element (changes the list to [1, 2, 6, 4, 5])
print('list after modifying:',my_list)