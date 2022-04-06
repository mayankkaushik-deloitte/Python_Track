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
    def second_problem(self):
        lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
        ans = list(map(lambda s : s if s.count('A') and s.count('a') else "", lst1))
        for each in ans:
            if each == '':
                ans.remove(each)
        print(ans)



obj = MapAndLambda()
# obj.first_problem()
obj.second_problem()