class FormulaError(Exception):
    length = 0
    operator = ''
    flag = 0
    def __init__(self, length, operator, flag):
        self.length = length
        self.operator = operator
        self.flag = flag
        pass
    def __str__(self):
        if self.length != 3:
            return "Formula Exception : The length isn't right"
        if self.operator != '-' or self.operator != '+':
            return "Formula Exception : The operator is incorrect, use '-' or '+'"
        if self.flag == 1:
            return "Formula Exception : The conversion threw an error."
def calc(str):
    arr = str.split(' ')
    try:
        if len(arr) != 3:
            raise FormulaError(len(arr),arr[1], 0)
    except FormulaError:
        print("The length of input isn't quite right!")
    finally:
        print("The length is alright.")

    try:
        if arr[1] != '+' or arr[1] != '-':
            raise FormulaError(len(arr),arr[1], 0)
    except FormulaError as e:
            print(e)
    try:
        operand1 = float(arr[0])
        operand2 = float(arr[2])
    except ValueError as e:
        raise FormulaError(len(arr), arr[1], 1)
    finally:
        if arr[1] == '+':
            print(operand1 + operand2)
        else:
            print(operand1 - operand2)





calc("1 * 2")