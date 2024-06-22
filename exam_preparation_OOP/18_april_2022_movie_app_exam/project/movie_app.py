from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        if self._find_user_by_username(username, self.users_collection) is not None:
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        found_user = self._find_user_by_username(username, self.users_collection)
        if found_user is None:
            raise Exception("This user does not exist!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        found_user.movies_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for movie_attribute, new_value in kwargs.items():
            if movie_attribute == "title":
                movie.title = new_value
            elif movie_attribute == "year":
                movie.year = int(new_value)
            elif movie_attribute == "age_restriction":
                movie.age_restriction = int(new_value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        found_user = self._find_user_by_username(username, self.users_collection)
        found_user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        found_user = self._find_user_by_username(username, self.users_collection)

        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in found_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        found_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        found_user = self._find_user_by_username(username, self.users_collection)

        if movie not in found_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        found_user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        output = []
        sorted_movies = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))

        if sorted_movies:
            for movie in sorted_movies:
                output.append(movie.details())
        else:
            output.append("No movies found.")

        return '\n'.join(output)

    def __str__(self):
        output = []

        all_usernames = [user.username for user in self.users_collection]
        all_movies = [movie.title for movie in self.movies_collection]

        if all_usernames:
            output.append(f"All users: {', '.join(all_usernames)}")
        else:
            output.append("All users: No users.")

        if all_movies:
            output.append(f"All movies: {', '.join(all_movies)}")
        else:
            output.append("All movies: No movies.")

        return '\n'.join(output)


    # HELPER METHODS

    @staticmethod
    def _find_user_by_username(username, collection):
        user = [user for user in collection if user.username == username]
        return user[0] if user else None

    @staticmethod
    def _find_movie_by_title(title, collection):
        movie = [movie for movie in collection if movie.title == title]
        return movie[0] if movie else None