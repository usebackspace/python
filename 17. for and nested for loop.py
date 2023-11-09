text = "Hello how"
for x in text:
    print(x)

print('-------- Nested For loop ----------')
# Nested For Loop
print('-------- Printing Inner loop And Outer Loop----------')

for i in range(3):
    print('Outer Loop')
    for j in range(1, 4):
        print('Innner loop')
    print('Another Loop Started')  


print('-------- Printing Table Using For Loop ----------')

x=11
for i in range(1,11):
    
    print(x,'*',i,'=',i*x)

print('-------- Printing Table Using Nested For Loop ----------')

for i in range(1, 3):
    for j in range(1, 11):
        result = i * j
        print(i ,'*', j ,'=', result)
    print()  # Add an empty line to separate each row

x=11
for i in range(1,11):
    print(x,'*',i,'=',i*x)