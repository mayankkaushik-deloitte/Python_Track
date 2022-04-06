class FRZ:
    def __init__(self):
        pass
    def fun(self):
        x

    def func(self,x):
        return -x if x < 0 else x
    def first_problem(self):
        lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
        ans = list(map(lambda x : -x,list(filter((lambda x : x < 0), lst1))))
        print(ans)

obj = FRZ()
obj.first_problem()