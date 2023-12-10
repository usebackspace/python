from functools import reduce

print('---- Addtion Of Number -----')
numbers = [1, 2, 3, 4, 5]

sum_result = reduce(lambda x, y: x + y, numbers,)

print("Sum:", sum_result)

print()

#========================================================================================================

print('---- Largest Number -----')

numbers = [3, 1, 4, 1, 5, 9, 2]

max_value = reduce(lambda x, y: x if x > y else y, numbers)

print("Maximum Value:", max_value)

print()

#========================================================================================================
print('---- Factorial of a number-----')
n = 5

factorial = reduce(lambda x, y: x * y, range(1, n + 1))

print("Factorial of", n, "is", factorial)

