# x=5
# for i in range(x):
#     print((lambda i:f"{i} even" if i%2==0 else f"{i} odd")(i))
    

print((lambda x: (lambda y: x - y))(5)(3))
