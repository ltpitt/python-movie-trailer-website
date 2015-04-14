#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This application creates a Movie Trailer Website from data entered in entertainment_center.py."""

__appname__ = "Movie Trailer Website"
__author__ = "Davide Nastri"
__version__ = "0.1beta"
__license__ = "GNU GPL 3.0"

import media
import fresh_tomatoes


THE_MATRIX = media.Movie("The Matrix",
                         "150 minutes",
                         "The world isn't real. Or it is?",
                         "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

THE_SOCIAL_NETWORK = media.Movie("The Social Network",
                                 "121 minutes",
                                 "Programming is coolest thing out there",
                                 "http://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                                 "https://www.youtube.com/watch?v=lB95KLmpLR4")

TRON_LEGACY = media.Movie("Tron Legacy",
                          "127 minutes",
                          "The son of a guy enters into a videogame with cool music & bikes",
                          "http://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg",
                          "https://www.youtube.com/watch?v=L9szn1QQfas")

movies = [THE_MATRIX, THE_SOCIAL_NETWORK, TRON_LEGACY]

fresh_tomatoes.open_movies_page(movies)