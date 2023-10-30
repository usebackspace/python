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

