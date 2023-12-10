print('---- Applying filter() in Normal Function ----')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)

print()

#======================================================================================================

print('---- Applying filter() in Lambda Function ----')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x:x%2==0, numbers))
print(even_numbers)

print()

#======================================================================================================

print('----- Checking string is Empty or Not -----')
strings = ["", "hello", "", "world", ""]

non_empty_strings = list(filter(lambda s: len(s) > 0, strings))
print(non_empty_strings)

print()

#======================================================================================================

print('---- Using Null in filter() ------')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [True,False,True,False,True]

even_numbers = list(filter(None, numbers))
print(even_numbers)

print()

#======================================================================================================
