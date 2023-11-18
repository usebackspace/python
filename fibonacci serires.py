n1=0
n2=1
n3=0
x= int(input("Enter the Number: "))
print(n1,n2,end=',')
for i in range(2,x):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=',')

def fibonacci_iterative(n):
    fib_series = [0, 1]

    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])

    return fib_series

# Example: Generate Fibonacci series up to 10 terms
result = fibonacci_iterative(10)
print(result)
