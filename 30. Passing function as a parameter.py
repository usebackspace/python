
print('-----1. Passing Function As A Parameter-----')
def display(sh):
    return"This is a Display Function: " + sh()
    # print("This is a Display Function: " ), show()


def show():
    return('This is a Show Function')
    # print('This is a Show Function')

print(display(show))
# display(disp)

print()

#===========================================================================

print('-----2. Passing Function As A Parameter-----')
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def operate(operation, x, y):
    return operation(x, y)

result1 = operate(add, 5, 3)
print("Result of addition:", result1)  # This will print "Result of addition: 8"

result2 = operate(subtract, 8, 2)
print("Result of subtraction:", result2)  # This will print "Result of subtraction: 6"
