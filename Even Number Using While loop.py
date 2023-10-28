# write a program to print even number between 100 and 200 using while loop

i=100
while(i<=200):
    if (i%2==0):
        print(i,"is a Even number.")
    i+=1

print('-------------- Even Number Using For loop---------------')
for x in range(100,201):
    if(x%2==0):
        print(x,'is a Even number')