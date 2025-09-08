class Cinema:
    def __init__(self,movies):
        self.movies=movies
    def book(self,movie,seats):
        self.movies[movie]-=seats
        return f"Booked {seats} tickets for {movie}"
    def cancel(self,movie,seats):
        self.movies[movie]+=seats
        return f"Cancelled {seats} tickets for {movie}"
    def show_movies(self):
        print(self.movies)
cinema = Cinema({"Avatar": 10, "Batman": 5})
print(cinema.book("Avatar", 2))
print(cinema.cancel("Avatar", 1))
cinema.show_movies()