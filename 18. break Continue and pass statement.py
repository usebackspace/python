# Applying Break Using For loop

for i in range(5):
    if(i==3):
        break
    print(i)



print('------Applying break using while loop--------')
# Applying Break Using while loop

i=1
while(True):
    if(i==3):
        break
    print(i)
    i+=1


print('-------- Continue Statement Start Here -------')

# Applying Continue Using For loop

for i in range(5):
    if(i==3):
        continue
    print(i)



print('------Applying Continue using while loop--------')
# Applying Continue Using while loop

i=0
while(i<10):
    i+=1
    if(i==3):
        continue
    print(i)
    


print('-------- Pass Statement Start Here -------')

# Applying Pass Using For loop
for i in range(10):
    if(i%2==0):
        pass
    else:
        print('Odd Number is',i)


