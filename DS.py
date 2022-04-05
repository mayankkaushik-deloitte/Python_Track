class DS:
    def __init__(self):
        pass
    def duplicates(self):
        n = int(input("Enter the size of the list of lists :: "))
        arr = [[] for i in range(n)]
        for i in range(n):
            dict = {}
            arr[i] = list(map(int, input("elements of array:-").strip().split()))
            for j in range(len(arr[i])):
                if arr[i][j] in dict:
                    dict[arr[i][j]] = dict[arr[i][j]] + 1
                else:
                    dict[arr[i][j]] = 1
            for key, val in dict.items():
                if val > 1 :
                    print(key, "-->", val)
    def mergeList(self):
        arr1 = list(map(int,input("elements of array:-").strip().split()))
        arr2 = list(map(int,input("elements of array:-").strip().split()))
        print(arr1 + arr2)
    def appendNested(self):
        list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
        list1[2][1][2].extend(["h", "i", "j"]);
        print(list1)

obj = DS()
# obj.duplicates()
# obj.mergeList()
obj.appendNested()