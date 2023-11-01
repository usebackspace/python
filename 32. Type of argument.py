
print('-------- Positional Argument ------------')
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Roger", 30)  # "Roger" and 30 are positional arguments.

print()

#==============================================================================

print('-------- Keyword Argument------------')

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(age=30, name="Roger")  # "Roger" and 30 are keyword arguments.

print()

#==============================================================================

print('--------- Default Argument ------------')
def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old.")

greet("Tony",)  # "Tony" is a positional argument; age uses its default value of 25.

#==============================================================================

print('------- Variable length argument --------')

print('--Example 1--')
def show(ar,ag2):
    print(ar,ag2)
show(100,200)

print()

print('--Example 2--')
def show(*args):
    print(args[1],args[0])
show(100,200)

print()

print('--Example 3--')
def show(*args):
    print(args[0],args[1])
show(100,200,300,400)

print()

print('--Sum Of Argument Passed--')
def sum_all(*args):
    result = 0
    for num in args:
        result = result+ num
    return result

print('Sum of All Argument Passed: ',sum_all(1, 2, 3, 4, 5))  # Any number of positional arguments can be passed.

print()

#==============================================================================

print('-- Keyword Variable Length Argument --')

print('--Example 1--')
def show(args,args2):
    print(args,args2)
show(100,200)

print()

print('--Example 2--')
def show(**args):
    print(args['a'],args['b'])
show(a=100,b=200)

print()

print('--Example 3--')
def show(**args):
    print(args['a'],args['c'])
show(a=100,b=200,c=300,d=400)

print()

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="John", age=30, city="New York")  # Any number of keyword arguments can be passed.

print()

