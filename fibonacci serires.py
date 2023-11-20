n1=0
n2=1
n3=0
x= int(input("Enter the Number: "))
print(n1,n2,end=',')
for i in range(1,x):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=',')

