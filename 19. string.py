string1 = 'This is a string.'
string2 = "This is another string."

print(string1 + string2)
print(string1, string2)

print()

print('--------Length of A string-----------')

# Length Of A String 
my_string = "Hello, World!"
length = len(my_string)
print(length)

print()

print('-------------Slicing of String----------')

# Slicing of String
print(my_string[1:12:2])      
print(my_string[1:12])  


print()

print('-------Accessing String Using for Loop------------')
# Accessing String Using For loop
x='Avengers'
for i in x:
    print(i)

print()

print('-----2nd Method-------')
for i in 'Avengers':
    print(i)

print()

print('------3rd Method------')
x='Avengers'
y=len(x)
for i in range(y):
    print(x[i])


print()

print('-------4th Method--------')
x='Avengers'
for i in range(len(x)):
    print(x[i])


print()
print('---------Repetition Operator *--------')
print('Anvengers'*5)