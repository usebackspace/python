# Defining Function without Parameter
print('------Defining Function without Parameter-------')
def add():
    """This function adds two numbers."""
    x=10
    y=10
    result = x + y
    print("Addition of 10 + 10 without parameter: ",result)

# Function call
add()

print()

#========================================================================

# Defining Function with Parameter
print('------Defining Function with one Parameter-------')
y='john'
def name(x):
    print("My Name is : ",x)

# Function call
name(y)

print()
#------------------------------------------------------------------------------

# Defining Function with Parameter
print('--------Defining Function with Parameter-------')
def add_numbers(x, y):
    """This function adds two numbers."""
    result = x + y
    print("Addition of 5 + 5 with parameter: ",result)

# Function call
add_numbers(5, 5)

print()

#-------------------------------------------------------------------------------

# Defining multiple function and callling in one function
print('---- Defining multiple function and callling in one function---')
def multiply(x, y):
    print('multiplication', x * y)

def add(x, y):
    print('Addition', x + y)

def subtract(x, y):
    print('Subtract', x - y)

# Input numbers
num1 = 2
num2 = 5

# Perform operations
def calculate():
    multiply(num1, num2)
    add(num1, num2)
    subtract(num1, num2)

# Display results
calculate()

