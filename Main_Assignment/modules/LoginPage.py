from Main_Assignment.modules.movieList import MovieList
from Main_Assignment.modules.userList import UserList
from Main_Assignment.modules.adminCRUD import Admin
from Main_Assignment.modules.userPage import UserPage


def user_login(movies: MovieList, users: UserList):
    print("************************** Welcome to User Login page *****************************")
    email = input("Email = ")
    password = input("Password = ")
    if email not in users.ulist.keys():
        print("No user present with this email address. Kindly go to the registration page")
        return
    if users.ulist[email].details['password'] != password:
        print("XXXXXXXXXXXXXXXXXXXXXXXXXX Wrong password XXXXXXXXXXXXXXXXXXXXXXXXX")
        return

    print("***********************Login successful*********************")
    user = users.ulist[email]

    print(f"***********************Welcome {user.details['name']}***********************")
    while True:
        lst = movies.get_movie_list()
        if len(lst) == 0:
            print("No movie has been registered yet")
            return
        for i in range(len(lst)):
            print(f"{i + 1}. {lst[i]}")
        inp = int(input("Enter the number corresponds to the movie = ")) - 1

        if inp >= len(lst) or inp < 0:
            print("Not a proper movie index")
            continue
        mv = movies.mlist[lst[inp]]
        print(mv)

        print("1. Book ticket")
        print("2. Cancel ticket")
        print("3. Give user rating")
        print("4. exit")
        inp = int(input())
        if inp == 1:
            print("choose timing")
            slots = mv.get_timings()
            for i in range(len(slots)):
                print(f"{i + 1}. {slots[i][0]} has {slots[i][1]} seats")
            inp = int(input()) - 1
            user.book_show(mv, slots[inp][0], int(input("No. of Seats = ")))
        elif inp == 2:
            print("choose timing")
            slots = mv.get_timings()
            for i in range(len(slots)):
                print(f"{i + 1}. {slots[i][0]} has {slots[i][1]} seats")
            inp = int(input()) - 1
            user.cancel_show(mv, slots[inp][0], int(input("No. of seats :: ")))
        elif inp == 3:
            user.give_user_rating(int(input("Give a number between 1 to 10 :: ")), mv)
            print("Avg. movie user 1rating = ", mv.get_user_rating())
        else:
            break


def admin_login(movies: MovieList):
    #init object of Admin class
    admin = Admin()
    try:
        if not admin.login(input("Username = "), input("Password = ")):
            raise Exception("Admin details incorrect")
    except Exception as e:
        print(e)
        return
    while True:
        print("========================******Welcome Admin*******====================")
        print("1. Add new Movie")
        print("2. Edit movie")
        print("3. Delete Movie")
        print("4. Logout")
        ip = input()
        if ip == '1':
            admin.add_movie(movies)#call add movie
        elif ip == '2':
            admin.edit_movie(movies)#call edit movie [Cannot edit title though]
        elif ip == '3':
            admin.delete_movie(movies)#call delete movie
        else:
            admin.logout()#call logout for admin
            return


def login(movies: MovieList, users: UserList):
    while True:
        print("=======================****** Welcome to BookMyShow Login *******======================")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Go Back")

        inp = input()
        if inp == '1':
            admin_login(movies)
        elif inp == '2':
            user_login(movies, users)
        else:
            break
