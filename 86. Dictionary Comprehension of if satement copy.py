print('---- 1.Even Number Using For loop -----')
for x in range(10):
    if x%2==0:
        print(x)

print('---- 1.Square of Even Number Using Dictionary Comprehension -----')
# Create a Dictionary of even numbers from 0 to 9
even_numbers = {x:x*2 for x in range(10) if x % 2 == 0}
print(even_numbers)

print()

#========================================================================================================== 

print('---- 2.Square Of Number Using For loop -----')
for x in range(10):
    if (x%2==0):
        print(x**2)


print('---- 2.Square of Number Using Dictionary Comprehension -----')
# Create a Dictionary of even numbers from 0 to 9
Square_numbers = {x**1:x**2 for x in range(10) if x % 2 == 0}
print(Square_numbers)

print()

#========================================================================================================== 
