class MapAndLambda:
    def __init__(self):
        pass
    def first_problem(self):
        a = int(input("Enter the value of a :: "))
        b = int(input("Enter the value of b :: "))
        c = int(input("Enter the value of c :: "))
        x = int(input("Enter the value of x :: "))
        lambdaAns = lambda a,b,c,x : a * x * x + b * x + c
        print(lambdaAns(a,b,c,x))



obj = MapAndLambda()
obj.first_problem()