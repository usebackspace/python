my_dict = {'a': 1, 'b': 2, 'c': 3, 1:'Kakarot',2:'Goku'}

# when We access dictionary it will only return keys of the dictionaries
print('---- Accessing Dicitonary using For loop ----')
for key in my_dict:
    print(key)

print()

print('----Iterate through keys----')
for key in my_dict:
    print(key, my_dict[key])

print()

print('---- Using items() method to iterate through key-value pairs----')
for key, value in my_dict.items():
    print(key, value)
