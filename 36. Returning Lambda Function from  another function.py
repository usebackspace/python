#==================================================================================
print('------ 1.Returning Lambda Function from Another Function ---------')

def lamb(x):
    return(f'Result of Return lambda function is {x(5)}')

print(lamb(lambda y:y*5))

print()

#==================================================================================
print('------ 2.Returning Lambda Function from Another Function ---------')

def power_function(exponent):
    return lambda x: x ** exponent

square = power_function(2)
result = square(5)  # This will calculate 5^2 = 25
print(result)

print()

#==================================================================================
print('------ 3.Returning Lambda Function from Another Function ---------')

def operation_function(operation):
    if operation == 'add':
        return lambda x, y: x + y
    elif operation == 'subtract':
        return lambda x, y: x - y
    else:
        return lambda x, y: x * y

add_function = operation_function('add')
result = add_function(10, 5)  # This will add 10 and 5
print(result)

print()

