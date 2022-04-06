from functools import reduce


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
    def second_problem(self):
        lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
        print(reduce(lambda x, y : x * y, lst1))
    def third_problem(self):
        lst1 = ["Netflix", "Hulu", "Sling", "Hbo"]
        lst2 = [198, 166, 237, 125]
        zipAns = zip(lst1,lst2)
        print(dict(zipAns))

obj = FRZ()
obj.first_problem()
obj.second_problem()
obj.third_problem()