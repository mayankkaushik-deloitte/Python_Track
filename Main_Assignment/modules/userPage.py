from Main_Assignment.modules.movie import Movie


class UserPage:
    def __init__(self, name, email, phone, age, password):
        self.details = {'name': name, 'email': email, 'phone': phone, 'age': age, 'password': password}
        self.bookings = dict()  # this will store timing and seats for each title

    def show_all_bookings(self) -> list:
        # returns a list of all the bookings and their title
        res = list(self.bookings.keys())
        for i in range(len(res)):
            print(f"{i + 1}. {res[i]}")
        return res

    def cancel_show(self, movie: Movie, timing: str, seats: int):
        print(self.bookings)
        title = movie.movie_details['title']
        if title not in self.bookings:
            print(f"No booking of {title} movie")
            return
        if timing not in self.bookings[title]:
            print(f"You have no booking of {title} at {timing} slot")
            return

        if seats > self.bookings[title][timing]:
            print("You are trying to cancel more seats than you have booked")
        else:
            self.bookings[title][timing] -= seats  # reduction of seats booked by us
            movie.time_slot[timing] += seats  # increment in left seats
            if self.bookings[title][timing] == 0:
                self.bookings[title].pop(timing)  # we remove a particular time slot if we dont have any booking for it
            if len(self.bookings[title]) == 0:
                self.bookings.pop(title)
            print("Cancellation successful")

    def show_timings(self, title: str):
        # show all the timings corresponding to a specific title
        res = list(self.bookings[title].keys())
        for i in range(len(res)):
            print(f"{i + 1}. {res[i]}")
        return res

    def book_show(self, movie: Movie, timing: str, seats: int):
        # book show and it handles the seats and timing allocation for each movie and user
        if movie.time_slot[timing] >= seats:
            movie.time_slot[timing] -= seats
            title = movie.movie_details['title']
            if title in self.bookings:
                if timing in self.bookings[title]:
                    self.bookings[title][timing] += seats
                else:
                    self.bookings[title][timing] = seats
            else:
                self.bookings[title] = {timing: seats}
            print(seats, "seats have been booked!")
        else:
            print("Enough seats are not available!")

    def give_user_rating(self, rating: int, movie: Movie):
        rating = max(1, rating)
        rating = min(10, rating)
        title = movie.movie_details['title']
        if title not in self.bookings:
            print("You haven't watch the movie yet")
            return
        movie.add_user_rating(rating)
        print("User rating added")

    def show_booking_details(self):
        for k, v in self.bookings.items():
            print(f"{k} => {v}")
