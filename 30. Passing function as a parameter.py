
print('-----1. Passing Function As A Parameter-----')
def display(show):
    return"This is a Display Function: " + show()
def disp():
    return('This is a Show Function')
print(display(disp))

print()

#===========================================================================

print('-----2. Passing Function As A Parameter-----')
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def apply_operation(func, a, b):
    # Call the provided function (func) with arguments (a, b)
    result = func(a, b)
    return result

# Pass the 'add' function as a parameter to 'apply_operation'
result1 = apply_operation(add, 5, 3)

# Pass the 'subtract' function as a parameter to 'apply_operation'
result2 = apply_operation(subtract, 5, 3)

print("Result of addition:", result1)
print("Result of subtraction:", result2)
