from modules import LoginPage
from modules import RegisterPage
from modules import *
movieObj = movieList()
userObj = userList()

while 1:
    print("******Welcome to BookMyShow*******")
    print("1. Login")
    print("2. Register new Account")
    print("3. exit")

    option = input("Enter the option you want to choose :: ")
    if option == 1:
        LoginPage.loginShow(movieObj, userObj)
    elif option == 2:
        registerShow(movieObj, userObj)
    else:
        exit(1)
