print('------ 1st Lambda Function ---------')
add_lambda = lambda x: (lambda y: x + y)
innerlambda = add_lambda(10) # Value 10 is for outer lambda function i.e x=10
result =innerlambda(70) # Value 70 is for inner lambda function i.e y=70
print(result)  # Output will be 80

print()

#==================================================================================
print('------ 2nd Lambda Function ---------')

sub_lambda = lambda x: (lambda y: x - y)
result = sub_lambda(10)(5) # Value 10 is for x ,and value 5 is for y
print(result)  # Output will be 5

print()


#==================================================================================
print('------ 3rd Lambda Function ---------')

product_lambda = lambda x: (lambda y: (lambda z: x * y * z))

result = product_lambda(2)(3)(4)
print(result)  # Output will be 24
