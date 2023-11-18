print('------ Printing With Normal Function -----')
def display(x):
    print(x)
display('Hello How are you!')

print()

#=================================================================================
print('------ Printing With Lambda Function -----')
y=lambda x : print(x)
y('Avengers')

print()

#===================================================================================
print('---- Adding 2 number With Lammbda Function ------')
add = lambda x,y:(x+y)

print(add)
print(add(5,6))

print()

#====================================================================================
print('------ Adding, Subtraction, Multiplication in one Lambda function  -----')
add_sum_mul = lambda x,y:(x+y,x-y,x*y)
print(add_sum_mul(5,6)) # Output will result in tuple

print()

print('-------Storing Result in variable in --------')
mix = lambda x,y:(x+y,x-y,x*y)
a,s,m=mix(5,6)
print(a)
print(s)
print(m)

print()

print('----- Passing Default Argument to the Lambda function -----')
add = lambda x,y=20:(x+y)
print(add(5,8))

print()