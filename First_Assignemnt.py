import string


class StringClass:
    s = ""

    def __init__(self):
        self.s = input()

    def length(self):
        return len(self.s)

    def convert(self):
        arr = []
        for char in self.s:
            arr.append(char)
        return arr


class PairsPossible(StringClass):
    arr = []
    s = "dasdasdasd"

    def __init__(self):
        self.s = input()
        pass

    def storeList(self):
        for i in range(len(self.s)):
            for j in range(i + 1, len(self.s)):
                self.arr.append(self.s[i] + self.s[j])

    def printList(self):
        for i in range(len(self.arr)):
            print(self.arr[i] + " ", end='')


class SearchCommonElements:
    StringClassString = ""
    PairPossibleString = ""

    arr = []
    def __init__(self, a, b):
        self.StringClassString = a
        self.PairPossibleString = b

    def common(self):
        dict = {}
        for char in self.StringClassString:
            if char in dict:
                continue
            else:
                dict[char] = 1;
        for char in self.PairPossibleString:
            if char in dict:
                self.arr.append(char)

    def printList(self):
        print(self.arr)


StringObj = StringClass()
print(StringObj.length())
print(StringObj.convert())
pairs = PairsPossible()
pairs.storeList()
pairs.printList()
third = SearchCommonElements(StringObj.s, pairs.s)
third.printList()