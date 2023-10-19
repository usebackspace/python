if (5<4):
    print('greater')
else:
    print('smaller')

# Nested if else

if (5<4):
    print(' 5 is greater')
else:
    if (6>7):
        print('6 is smaller')
    else:
        print('7 is greater')


# Another Nested If else example
age = 20
license = True

if age >= 18:
    if license:
        print("You are eligible to drive.")
    else:
        print("You are of legal age, but you don't have a driver's license.")
else:
    print("You are too young to drive.")
