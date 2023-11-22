print('---- Factorial, Using Recursive Function ----')
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

n=5
print(f'factorial of {n} is : {factorial(n)}')

print()

#=======================================================================================
print('---- Fibonacci, Using Recursive Function ----')
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n=5
print(f'Fibonacci series of {n} is : {fibonacci(n)}')

print()
#==========================================================================================
print('---- Sum of digit, Using Recursive Function ----')

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


