class Loops:
    val = 0
    def __init__(self, val):
        self.val = val
    def print_pascals_traingle(self):
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
                print(arr[i][j], end='')
            print()


LoopOBJ = Loops(5)
LoopOBJ.print_pascals_traingle()