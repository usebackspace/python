i=1
while(i<4):
    print('While loop')
    i=i+1

print('-----Nested While Loop--------')
# Nested While loop
i=1
while(i<4):
    print('Innner loop',i)
    i=i+1
    j=1
    while(j<3):
        print('outer loop',j)
        j+=1



n=5
while(n):
    n=n-1
    print(n,end=' ')



t=(1,2,4,3,8,9)
print([t[i] for i in range(0,len(t),2)])


for k in  range(1,101):
    if int(i*0.5)==k*0.5:
        print(i)

print([k for k in range(1,101) if int(i*0.5)==k*0.5])



print('------------------------')

x=50
def f(x):
    print('x ix',x)
    x=2
    print('x in fuc',x)
print("cahnage x to",x)
f(x)
print('x ix now ',x)