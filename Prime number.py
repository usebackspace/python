x=int(input("Enter Any Number: "))
if(x<=1):
    print("It is not a prime number")
else:
    if(x==2):
        print("It is a prime number")
    else:
        i=2
        while(i<x):
            if(x%i==0):
               y=0
               break
            else:
                y=1
            i+=1
if(y==1):
    print("It is a prime Number")
else:
    print("It is not a prime Number")


print()


print('--------Prime Number With Function----------')

def prime(x):
    if (x<=1):
        return False
    else:
        for i in range(2,x):
            if(x%i==0):
                return True
        return False
x=prime(9)
if(x==True):
    print("It Is Not A Prime Number")
else:
    print("It Is A Prime Number")

