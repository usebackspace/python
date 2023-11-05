print('------Normal if else condition-----------')
if (5<4):
    print('greater')
else:
    print('smaller')

print()

#=====================================================================

# Nested if else
print('-------Nested if else statement------------')
if (5<4):
    print(' 5 is greater')
    if (6<7):
        print('6 is smaller')
    else:
        if(7>8):
            print('7 is smaller')
        else:
            print('8 is greater')

print()

#=======================================================================

# Another Nested If else example

print('------------Liscence if else Condition----------------')
age = 20
license = False

if age >= 18:
    if license:
        print("You are eligible to drive.")
    else:
        print("You are of legal age, but you don't have a driver's license.")
else:
    print("You are too young to drive.")
