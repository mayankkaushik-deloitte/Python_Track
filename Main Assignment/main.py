import sys
sys.path.append("C:\\Users\\mayakaushik\\Python Track\\Main Assignment\\LoginPage.py")
sys.path.append("C:\\Users\\mayakaushik\\Python Track\\Main Assignment\\RegisterPage.py")
import LoginPage
import RegisterPage


class MAIN():
    option = 0

    def __init__(self):
        pass

    def welcome(self):
        print("*************WELCOME to BOOKMYSHOW*************")

    def showOptions(self):
        print("1. Login")
        print("2. Register")
        print("3. Exit")

    def askForInput(self):
        self.option = int(input("Please enter one of the above options :: "))
        return self.option


process = MAIN()
process.welcome()
process.showOptions()
option = process.askForInput()
while option != 3:
    if option == 1:
        LoginPage.obj.get_existing_users()
        if LoginPage.obj.checkIfExists():
            print("You are logged in!")
        else:
            print("Try signing in first")

    else:
        RegisterPage.obj.show()
    process.showOptions()
    option = process.askForInput()
print("Thanks you!")
