class MAIN():
    option = 0
    def __init__(self):
        pass
    def welcome(self):
        print("*************WELCOME to BOOKMYSHOW*************")
    def showOptions(self):
        self.welcome()
        print("1. Login")
        print("2. Register")
        print("3. Exit")
    def askForInput(self):
        self.option = int(input("Please enter one of the above options :: "))
        return self.option

process = MAIN()
process.showOptions()
option = process.askForInput()
while option != 3:
    if option == 1:
        
    else:


