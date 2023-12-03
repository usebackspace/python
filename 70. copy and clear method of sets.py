print('---- Copy Method ----')

numbers_set = {1, 2, 3, 4, 5}
copied_set = numbers_set.copy()

print("Original Set:", numbers_set)
print("Copied Set:", copied_set)

copied_set.add(6)

print()

print("Original Set after modification:", numbers_set)
print("Copied Set after modification:", copied_set)

print()

#==================================================================================================================

print('---- Clear Method ----')

numbers_set = {1, 2, 3, 4, 5}
numbers_set.clear()

print("Set after clear:", numbers_set)
