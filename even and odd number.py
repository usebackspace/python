x=5
for i in range(x):
    y =(lambda i:f"{i} even" if i%2==0 else f"{i} odd")
    print(y(i))
    print((lambda i:f"{i} even" if i%2==0 else f"{i} odd")(i))