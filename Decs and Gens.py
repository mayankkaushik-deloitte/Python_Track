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
def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        yield 0
        yield 1

    first = 0
    yield first
    second = 1
    yield second
    count = 3
    while count <= n:
        next = first + second
        yield next
        first = second
        second = next
        count = count + 1
values = fibo(50)
for i in values:
    print(i)