print('---- 1.Number Divisible by 3 and 7 Using For loop -----')
for x in range(100):
    if x % 3==0:
        if x % 7==0:
            print(x)

print('---- 1.Number Divisible by 3 and 7 Using Dictionary Comprehension -----')

even_numbers = {x:x*3 for x in range(100) if x % 3 == 0 if x % 7==0}
print(even_numbers)

print()

#========================================================================================================== 

print('---- 2.Square Of Number Using For loop -----')
for x in range(100):
    if (x % 3==0):
        if(x % 7==0):
            print(x**2)


print('---- 2.Square of Number Using Dictionary Comprehension -----')
# Create a Dictionary of even numbers from 0 to 9
Square = {x*2:x*3 for x in range(100) if x % 3 == 0 if x % 7==0}
print(Square)

print()

#========================================================================================================== 
