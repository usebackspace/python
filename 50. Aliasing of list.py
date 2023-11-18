
original = [1, 2, 3]
print('-------Original list------')
print(original)

alias = original

original.append(4)
# Both lists are now modified because they refer to the same object
print('----- After Appending in original List, changes will Reflect on both object------')
print('original: ',original)  # Output: [1, 2, 3, 4]
print('alias: ',alias)     # Output: [1, 2, 3, 4]

print('----- After Appending in alias List, changes will Reflect on both object------')
alias.append(5)
# Both lists are now modified because they refer to the same object
print('original: ',original)  # Output: [1, 2, 3, 4, 5]
print('alais: ',alias)     # Output: [1, 2, 3, 4, 5]
