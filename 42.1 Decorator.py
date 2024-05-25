def decorate(x):
    def wrap():
        print("Before the function is called.")
        x()
        print("After the function is called.")
    return wrap

def Aven():
    print("Avengers")

result =decorate(Aven)
result()

print()

print('------------------------------------')

def decorate(func):
    def wrap():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrap

@decorate
def Aven():
    print("Avengers")

Aven()


