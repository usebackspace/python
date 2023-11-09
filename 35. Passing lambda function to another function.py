#==================================================================================
print('------ 1.Passing Lambda Function To The Another Function ---------')

def lamb(x):
    print(f'Result of lambda function is {x(5)}')
lamb(lambda y:y*5)

print()

#==================================================================================
print('------ 2.Passing Lambda Function To The Another Function ---------')

increment = lambda x: x + 10
square = lambda x: x * x
def apply_function(func,number):
    return func(number)

result1 = apply_function(increment,5)
result2 = apply_function(square,5)

print(result1)  # Output: 6
print(result2)  # Output: 25

print()
