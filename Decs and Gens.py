#===========DECORATORS=================
def my_dec(func):
    def inner (a, b):
        func(a,b)
        func(a,b)
    return inner
@my_dec
def multiply(a,b):
    print("Answer of multiplication is ::", a * b)
multiply(2,4)

#============GENERATORS===============
