#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This module contains classes and methods for the Movie Trailer Website application."""

__appname__ = "Movie Trailer Website"
__author__ = "Davide Nastri"
__version__ = "0.1beta"
__license__ = "GNU GPL 3.0"

import webbrowser

class Video():
    """ Parent class """

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """ Video's child class containing a Movie variables and methods """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, duration, storyline, poster_image, trailer_youtube):
        Video.__init__(self, title, duration)
        self.movie_storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Opens a trailer
        """
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Movie):
    """ Movie's child class containing a TvShow variables and methods """

    def __init__(self, title, duration, storyline, poster_image, trailer_youtube):
        Movie.__init__(self, title, duration, storyline, poster_image, trailer_youtube)
