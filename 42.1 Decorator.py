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

print()

print('--------------')
def girlfriend(liya):
    def gift_bf():
        a='Flower '
        r=a+liya()
        return r
    return gift_bf

def ex(liya):
    def gift_gf():
        x='car '
        r=x+liya()
        return r
    return gift_gf

@ex
@girlfriend
def gift():
    return "Ring"

# gift =ex(girlfriend(gift))
print(gift())
