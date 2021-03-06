class Loops:
    val = 0

    def __init__(self, val):
        self.val = val

    def print_pascals_triangle(self):
        # 1 0 0 0
        # 1 1 0 0
        # 1 2 1 0
        # 1 3 3 1
        rows, cols = (self.val, self.val)
        arr = [[0 for j in range(cols)] for i in range(rows)]
        arr[0][0] = 1
        for i in range(1, rows):
            arr[i][0] = 1
            for j in range(1, cols):
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
        print("The triangle is : ")
        for i in range(rows):
            for j in range(cols):
                print(str(arr[i][j]) + " ", end='')
            print()
    def first_pattern(self):
        arr = [[0 for i in range(self.val)] for j in range(self.val)]
        n = self.val
        start = 1
        for i in range(int(n / 2)):
            for j in range(int(n / 2) - i):
                print(" ", end = '')
            for j in range(start):
                print("*", end = '')
            start = start + (2 if n % 2 == 1 else 1)
            print()
        for i in range(n):
            print("*", end = '')
        print()
        start -= 2
        for i in range(int(n / 2) - (1 if n % 2 == 1 else 0), -1, -1):
            for j in range(int(n / 2) - i):
                print(" ", end = "")
            for j in range(start):
                print("*", end = "")
            start = start - (2 if n % 2 == 1 else 1)
            print()

    def second_pattern(self):
        row = self.val
        for i in range(row):
            for j in range(row - i):
                print(' ', end='')
            for j in range(2 * i + 1):
                if j == 0 or j == 2 * i or i == row - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    def thrid_pattern(self):
        arr = [[" " for i in range(self.val)] for j in range(self.val)]
        for i in range(self.val):
            for j in range(self.val):
                if i == 0:
                    arr[i][j] = 'a*'
                if i == j:
                    arr[i][j] = '*'
                if j == self.val - 1:
                    arr[i][j] = '*'
        for i in range(self.val):
            for j in range(self.val):
                print(arr[i][j], end = '')
            print()



LoopOBJ = Loops(9)
# Pascals part
LoopOBJ.print_pascals_triangle()
LoopOBJ.first_pattern()
LoopOBJ.second_pattern()
LoopOBJ.thrid_pattern()
