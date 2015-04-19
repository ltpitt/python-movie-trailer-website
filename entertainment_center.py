#!/usr/bin/python
# -*- coding: utf-8 -*-
""" This application creates a Movie Trailer Website from movie data entered.
"""

__appname__ = "Trailer Website"
__author__ = "Davide Nastri"
__version__ = "0.1beta"
__license__ = "GNU GPL 3.0"

import media
import fresh_tomatoes

# Parameters to create instance of a movie: title, duration, description, poster link, trailer link.
OFFICE_SPACE = media.Movie("Office space",
                           89,
                           "Three company workers who hate their jobs and decide to rebel against their greedy boss",
                           "http://upload.wikimedia.org/wikipedia/en/8/8e/Office_space_poster.jpg",
                           "https://www.youtube.com/watch?v=_IwzZYRejZQ")

WARGAMES = media.Movie("Wargames",
                       114,
                       "A young man enters into a military central computer, possibly starting World War III",
                       "http://upload.wikimedia.org/wikipedia/en/2/29/Wargames.jpg",
                       "https://www.youtube.com/watch?v=tAcEzhQ7oqA")

A_SPACE_ODYSSEY = media.Movie("2001: a space odyssey",
                              161,
                              "Humanity finds a mysterious, obviously artificial, object buried on the moon...",
                              "http://upload.wikimedia.org/wikipedia/en/e/ef/2001_A_Space_Odyssey_Style_B.jpg",
                              "https://www.youtube.com/watch?v=XHjIqQBsPjk")

PIRATES_OF_SILICON_VALLEY = media.Movie("Pirates of silicon valley",
                                        97,
                                        "The beginning of Apple and Microsoft",
                                        "http://upload.wikimedia.org/wikipedia/en/3/30/Movieposterposv.jpg",
                                        "https://www.youtube.com/watch?v=lEyrivrjAuU")

THE_MATRIX = media.Movie("The Matrix",
                         150,
                         "The world isn't real. Or it is?",
                         "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

HACKERS = media.Movie("Hackers",
                      107,
                      "A young boy is arrested by the U.S. Secret Service for writing a computer virus",
                      "http://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg",
                      "https://www.youtube.com/watch?v=vCobCU9FfzI")

THE_SOCIAL_NETWORK = media.Movie("The Social Network",
                                 121,
                                 "How a young relentless programmer changed the world of communication",
                                 "http://bit.ly/1DDuWL8",
                                 "https://www.youtube.com/watch?v=lB95KLmpLR4")

REVOLUTION_OS = media.Movie("Revolution OS",
                            85,
                            "GNU/Linux: the free Operating System history",
                            "http://upload.wikimedia.org/wikipedia/en/5/5e/Revolution_OS.jpg",
                            "https://www.youtube.com/watch?v=NrI-0u4npGo")

TRON_LEGACY = media.Movie("Tron Legacy",
                          127,
                          "The son of a guy enters into a videogame with cool music & bikes",
                          "http://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg",
                          "https://www.youtube.com/watch?v=L9szn1QQfas")

JOBS = media.Movie("Jobs",
                   122,
                   "The story of Steve Jobs, Apple Computer founder",
                   "http://upload.wikimedia.org/wikipedia/en/e/e0/Jobs_%28film%29.jpg",
                   "https://www.youtube.com/watch?v=LR6yMl2FZSQ")

# Creating a movies list to pass to the open_page function
MOVIES = [JOBS, REVOLUTION_OS, A_SPACE_ODYSSEY, WARGAMES, THE_MATRIX, THE_SOCIAL_NETWORK, TRON_LEGACY, HACKERS,
          PIRATES_OF_SILICON_VALLEY, OFFICE_SPACE]

# Ordering movies by movie title
MOVIES = sorted(MOVIES, key=lambda movie: movie.title)

BIGBANGTHEORY = media.TvShow("The Big Bang Theory",
                             8,
                             5500,
                             "Two brilliant and socially awkward physicists meet a woman that will change their life",
                             "http://bit.ly/1bbD1vs",
                             "https://www.youtube.com/watch?v=WBb3fojgW0Q",
)

ITCROWD = media.TvShow("The IT Crowd",
                       4,
                       625,
                       "The comedic adventures of a rag-tag group of technical support workers at a large corporation",
                       "http://www.tvposter.net/posters/the_it_crowd_2006_2885_poster.jpg",
                       "https://www.youtube.com/watch?v=YuzbJvxPSCk",
)

DOCTORWHO = media.TvShow("Doctor Who",
                         8,
                         1300,
                         "The adventures of a time traveling alien adventurer and his companions.",
                         "http://www.thedarehub.com/tv/thumbs/show_72525a1fb17068fa8b451c428521086f.jpg",
                         "https://www.youtube.com/watch?v=TivqZTq5u6Y",
)

STARTREK = media.TvShow("Star Trek",
                        3,
                        900,
                        "Captain James T. Kirk and the crew of the Starship Enterprise explore the Galaxy",
                        "http://monsterislandnews.com/yahoo_site_admin/assets/images/star_trek.7074651_std.jpg",
                        "https://www.youtube.com/watch?v=nPDb5wX4H7I",
)

# Creating a movies list to pass to the open_page function
TVSHOWS = [BIGBANGTHEORY, ITCROWD, DOCTORWHO, STARTREK]

# Ordering movies by movie title
TVSHOWS = sorted(TVSHOWS, key=lambda tvshow: tvshow.title)

# Creating and opening in webbrowser the html page containing the movies
fresh_tomatoes.open_page(MOVIES, TVSHOWS)
