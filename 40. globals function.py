print('-----Using Globals Function------')
var = 10

def my_function():
    # var= 30
    print("Inside the function:", var)
    # x=globals()['var']
    # print(x)
my_function()

print("Outside the function:", var)

