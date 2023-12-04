print('---- Empty Dictionary ----')

empty_dict = {}
print(empty_dict)

print()

#==========================================================================================================

print('---- Dictionary syntax ----')
my_dict = {'Name ': 'Roger', 'Heoric Name': 'Captain America', 'Power': 'Sheild'}
print(my_dict)

print()

#==========================================================================================================

print('---- Dictionary Key ----')

my_dict = {'Name ': 'Roger', 'Heoric Name': 'Captain America', 'Power': 'Sheild'}

numeric_dict = {1: 'one', 2: 'two', 3: 'three'}

tuple_dict = {('a', 1): 'value1', ('b', 2): 'value2'}

print(my_dict)
print(numeric_dict)
print(tuple_dict)

print()

#==========================================================================================================

print('---- Dictionary Values ----')

string_values = {'name': 'John', 'age': 25, 'city': 'New York'}

list_values = {'numbers': [1, 2, 3], 'colors': ['red', 'green', 'blue']}

print(string_values)
print(list_values)

print('---- Overwrite Previous Value ---- ')

string_values['name']='Peter' # Represent mutable properties
print(string_values)

print()

#==========================================================================================================

print('----= Accessing Dictionary Values -----')

my_dict = {'Name': 'Roger', 'Heroic Name': 'Captain America', 'Power': 'Sheild'}

print(my_dict['Name'])
print(my_dict['Heroic Name'])
print(my_dict['Power'])
