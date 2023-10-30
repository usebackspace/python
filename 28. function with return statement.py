print('-----Display Function------')
def display():
    return "This is a Display function"
print(display())

print()

#--------------------------------------------------------------------

print('----Directly Printing Result------')
def add_numbers(x, y):
    """This function adds two numbers."""
    result = x + y
    return result

# Function call
print(add_numbers(5, 10))

print()

#-----------------------------------------------------------------------

print('-----Returning Function to the variable----')

def add_numbers(x, y):
    """This function adds two numbers."""
    result = x + y
    return result

# Function call
sum_result = add_numbers(5, 15)
print(sum_result)  # This will print "20"

print()

#-----------------------------------------------------------------------

print('-----Returning Function to the variable----')

def add_numbers(x, y):
    """This function adds two numbers."""
    add = x + y
    sub = x-y
    return add, sub

# Function call
x,y = add_numbers(5, 15)
print(x,y)  # This will print "20,-10"
