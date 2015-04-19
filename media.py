#!/usr/bin/python
# -*- coding: utf-8 -*-
""" This module contains classes and methods for the Movie Trailer Website application.
"""

__appname__ = "Trailer Website"
__author__ = "Davide Nastri"
__version__ = "0.1beta"
__license__ = "GNU GPL 3.0"

import webbrowser


class Video():
    """ Parent class
    """

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """ Video's child class containing Movie variables and methods
    """

    def __init__(self, title, duration, storyline, poster_image, trailer_youtube):
        """
        :param title: Movie title, string
        :param duration: Movie duration (in minutes), int
        :param storyline: Movie short plot, string
        :param poster_image: Movie poster image link, string
        :param trailer_youtube: Movie youtube trailer link, string
        :return:
        """
        Video.__init__(self, title, duration)
        self.movie_storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        """ Opens the trailer """
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Movie):
    """ Movie's child class containing a TvShow variables and methods
    """


    def __init__(self, title, seasons, duration, storyline, poster_image, trailer_youtube):
        """
        :param title: TvShow title, string
        :param seasons: TvShow total seasons number, int
        :param duration: TvShow duration (in minutes), int
        :param storyline: TvShow short plot, string
        :param poster_image: TvShow poster image link, string
        :param trailer_youtube: TvShow youtube trailer link, string
        """
        Movie.__init__(self, title, duration, storyline, poster_image, trailer_youtube)
        self.seasons = seasons

