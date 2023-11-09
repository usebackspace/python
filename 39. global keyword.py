print('-----Using Global Keyword------')
var = 10

def my_function():
    global var
    # var=20
    var= var+10
    print("Inside the function:", var)

my_function()

print("Outside the function:", var)

