print('---- Palindrome Number ---')
def palindrome(n):
    sum = ""
    for i in n:
        sum = i+sum
    if sum==n:
        return 'Palindrome'
    else:
        return 'Not Palindrome'

num = input('Enter the number: ')
result = palindrome(num)
print(f"The number {num} is {result}")
