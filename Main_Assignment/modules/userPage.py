from Main_Assignment.modules.movie import Movie


class UserPage:
    def __init__(self, name, email, phone, age, password):
        self.details = {'name': name, 'email': email, 'phone': phone, 'age': age, 'password': password}
        self.bookings = dict()

    def show_all_bookings(self) -> list:
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
            self.bookings[title][timing] -= seats
            movie.time_slot[timing] += seats
            if self.bookings[title][timing] == 0: self.bookings[title].pop(timing)
            if len(self.bookings[title]) == 0: self.bookings.pop(title)
            print("Cancellation successful")

    def book_show(self, movie: Movie, timing: str, seats: int):
        if movie.time_slot[timing] >= seats:
            movie.time_slot[timing] -= seats
            title = movie.movie_details['title']
            if title in self.bookings:
                if timing in self.bookings[title]:
                    self.bookings[title][timing] += seats
                else:
                    self.bookings[title][timing] = seats
            else:
                self.bookings[title] = {title: seats}
            print(seats, "seats have been booked!")
        else:
            print("Enough seats are not available!")

    def show_booking_details(self):
        for k, v in self.bookings.items():
            print(f"{k} => {v}")
