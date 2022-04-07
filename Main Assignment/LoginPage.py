class LoginPage():
    username = ""
    password = ""
    DETAILS = "C:\\Users\\mayakaushik\\Python Track\\Main Assignment\\data\\test.txt"
    def __init__(self):
        pass
    def get_existing_users(self):
        with open(self.DETAILS, 'r') as fp:
            # print(fp.read())
            for line in fp.readlines():
                # This expects each line of a file to be (name, pass) seperated by whitespace
                arr = line.split(',')
                print(arr)
                yield arr[0], arr[1]
    def checkIfExists(self):
        username, password = self.show()
        return any(user == (username, password) for user in self.get_existing_users())

    def show(self):
        self.username = input("Enter the username :: ")
        self.password = input("Enter the password :: ")
        return self.username,self.password


obj = LoginPage()