# def decorate(Aven):
#     def wrap():
#         print("Before the function is called.")
#         Aven()
#         print("After the function is called.")
#     return wrap

# def Aven():
#     print("Avengers")

# Aven =decorate(Aven)
# Aven()

# print()

# print('------------------------------------')

# def decorate(func):
#     def wrap():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")
#     return wrap

# @decorate
# def Aven():
#     print("Avengers")

# Aven()

# print()

print('--------------')
def add(num):
    def wrap():
        a=10
        r=a+num()
        return r
    return wrap

def mul(num):
    def wrap():
        x=5
        r=x*num()
        return r
    return wrap

@mul
@add
def num():
    return 20

# num =mul(add(num))
print(num())
