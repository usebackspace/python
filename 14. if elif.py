# Example 1
print('-----1. elif statement--------')
if (5<4):
    print('5 is greater')
elif(4<3):
    print(' 4 is greater')
elif (6>7):
    print('6 is smaller')
else:
    print('7 is greater')

print()

#======================================================================

# Example 2
print('-----2. elif statement--------')

grade = 85

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

print()

#============================================================================
# Example of Nested elif 
print('-----3. elif statement--------')

temperature = 25
is_raining = True

if temperature > 30:
    if is_raining:
        print("It's hot, and it's raining. Consider staying indoors.")
    else:
        print("It's hot. Enjoy the sunshine!")
elif temperature > 20:
    if is_raining:
        print("It's warm, but it's raining. Don't forget your umbrella.")
    else:
        print("It's warm and sunny. Perfect weather!")
else:
    if is_raining:
        print("It's cool, and it's raining. Bring a jacket and an umbrella.")
    else:
        print("It's cool and dry. Grab a light jacket and enjoy the day.")
