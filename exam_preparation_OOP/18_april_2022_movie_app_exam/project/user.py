from typing import List

from project.movie_specification.movie import Movie


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: List[Movie] = []
        self.movies_owned: List[Movie] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        if len(value) == 0:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        liked_movies = [f"Username: {self.username}, Age: {self.age}", "Liked movies:"]
        owned_movies = [f"Username: {self.username}, Age: {self.age}", "Owned movies:"]

        if self.movies_liked:
            for movie in self.movies_liked:
                liked_movies.append(movie.details())
        else:
            liked_movies.append("No movies liked.")

        if self.movies_owned:
            for movie in self.movies_owned:
                owned_movies.append(movie.details())
        else:
            owned_movies.append("No movies liked.")

        final_output = []
        final_output.extend(liked_movies)
        final_output.extend(owned_movies)

        return '\n'.join(final_output)



