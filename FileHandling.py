def longestWordIdentification(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    maxLen = max(len(each) for each in words)
    return [word for word in words if len(word) == maxLen]


print(longestWordIdentification("C:\\Users\\mayakaushik\\Python Track\\data\\file.txt"))
