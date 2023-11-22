print('---- Sum of digit Using for loop ---')
def sum_of_digits(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

num = int(input('Enter the number: '))
result = sum_of_digits(num)
print(f"The sum of the digits of {num} is {result}")

print()

#================================================================================================
print('---- Sum of digit Using While loop ---')
def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

num = int(input('Enter the number: '))
result = sum_of_digits(num)
print(f"The sum of the digits of {num} is {result}")
