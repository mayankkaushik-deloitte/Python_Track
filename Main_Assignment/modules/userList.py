from Main_Assignment.modules.userPage import User


class UserList:
    def __init__(self):
        self.ulist = dict()

    def __str__(self):
        return str(set(self.ulist.keys()))

    def delete_user(self, name: str):
        try:
            self.ulist.pop(name)
        except:
            print("user not found, deletion unsuccessful")

    def addUser(self, user: User):
        self.ulist[user.details['email']] = user
