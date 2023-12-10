print('---- 1.Number Divisible by 3 and 7 Using For loop -----')
for x in range(100):
    if x % 3==0:
        if x % 7==0:
            print(x)

print('---- 1.Number Divisible by 3 and 7 Using set Comprehension -----')

even_numbers = {x for x in range(100) if x % 3 == 0 if x % 7==0}
print(even_numbers)

print()

#========================================================================================================== 

print('---- 2.Square Of Number Using For loop -----')
for x in range(100):
    if (x % 3==0):
        if(x % 7==0):
            print(x**2)


print('---- 2.Square of Number Using set Comprehension -----')
# Create a set of even numbers from 0 to 9
Square_numbers = {x**2 for x in range(100) if x % 3 == 0 if x % 7==0}
print(Square_numbers)

print()

#========================================================================================================== 
