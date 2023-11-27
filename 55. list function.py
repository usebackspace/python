print('---- String to the list ----')
my_string = "hello how are you"
string_list = list(my_string)
print(string_list)  # Output: ['h', 'e', 'l', 'l', 'o']

print()

print('---- Tuple to the list ----')
my_tuple = (1, 2, 3)
tuple_list = list(my_tuple)
print(tuple_list)  # Output: [1, 2, 3]

print()

print('---- Set to the list ----')
my_set = {1, 2, 3}
set_list = list(my_set)
print(set_list)  # Output: [1, 2, 3]

print()

print('---- Dictionary to the list ----')
my_dict = {'a': 1, 'b': 2, 'c': 3}
dict_keys_list = list(my_dict.keys())
dict_keys_list1 = list(my_dict.values())

print(dict_keys_list)  # Output: ['a', 'b', 'c']
print(dict_keys_list1)  # Output: ['1', '2', '3']

print()

print('---- Range to the list ----')
my_range = range(1, 5)
range_list = list(my_range)
print(range_list)  # Output: [1, 2, 3, 4]

