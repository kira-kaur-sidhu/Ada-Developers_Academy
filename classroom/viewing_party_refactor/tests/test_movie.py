import pytest
from viewing_party.movie import Movie

def test_movie_name_correctly():
    # Arrange/ Act
    movie = Movie("Cinderella", "animated", 2)
    
    # Assert
    assert movie.movie_name == "Cinderella"

def test_movie_genre_correctly():
    # Arrange/ Act
    movie = Movie("Cinderella", "animated", 2)

    # Assert
    assert movie.genre == "animated"

def test_movie_rating_correctly():
    # Arrange/ Act
    movie = Movie("Cinderella", "animated", 2)

    # Assert
    assert movie.rating == 2