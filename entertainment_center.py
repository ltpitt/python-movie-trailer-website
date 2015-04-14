#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This application creates a Movie Trailer Website from movie data entered."""

__appname__ = "Movie Trailer Website"
__author__ = "Davide Nastri"
__version__ = "0.1beta"
__license__ = "GNU GPL 3.0"

import media
import fresh_tomatoes

# Parameters to create instance of a movie: title, duration, description, poster link, trailer link.
PIRATES_OF_SILICON_VALLEY = media.Movie("Pirates of silicon valley",
                                        "97 minutes",
                                        "History of Apple and Microsoft.",
                                        "http://upload.wikimedia.org/wikipedia/en/3/30/Movieposterposv.jpg",
                                        "https://www.youtube.com/watch?v=lEyrivrjAuU")


THE_MATRIX = media.Movie("The Matrix",
                         "150 minutes",
                         "The world isn't real. Or it is?",
                         "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

HACKERS = media.Movie("Hackers",
                      "107 minutes",
                      "A young boy is arrested by the U.S. Secret Service for writing a computer virus",
                      "http://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg",
                      "https://www.youtube.com/watch?v=vCobCU9FfzI")

THE_SOCIAL_NETWORK = media.Movie("The Social Network",
                                 "121 minutes",
                                 "Programming is coolest thing out there",
                                 "http://bit.ly/1DDuWL8",
                                 "https://www.youtube.com/watch?v=lB95KLmpLR4")

TRON_LEGACY = media.Movie("Tron Legacy",
                          "127 minutes",
                          "The son of a guy enters into a videogame with cool music & bikes",
                          "http://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg",
                          "https://www.youtube.com/watch?v=L9szn1QQfas")

# Creating a list to pass to the open_movie_page function
MOVIES = [THE_MATRIX, THE_SOCIAL_NETWORK, TRON_LEGACY, HACKERS, PIRATES_OF_SILICON_VALLEY]

# Ordering movies by movie title
MOVIES = sorted(MOVIES, key=lambda movie: movie.title)

#Creating and opening in webbrowser the html page containing the movies
fresh_tomatoes.open_movies_page(MOVIES)
