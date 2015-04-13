#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This application creates a Movie Trailer Website from data entered in entertainment_center.py."""

__appname__ = "Movie Trailer Website"
__author__ = "Davide Nastri"
__version__ = "0.1beta"
__license__ = "GNU GPL 3.0"

import logging

log = logging.getLogger(__name__)

if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser(version="%%prog v%s" % __version__,
                          usage="%prog [options] <argument> ...",
                          description=__doc__.replace('\r\n', '\n').split('\n--snip--\n')[0])
    parser.add_option('-v', '--verbose', action="count", dest="verbose",
                      default=2, help="Increase the verbosity. Use twice for extra effect")
    parser.add_option('-q', '--quiet', action="count", dest="quiet",
                      default=0, help="Decrease the verbosity. Use twice for extra effect")
    # Reminder: %default can be used in help strings.

    # Allow pre-formatted descriptions
    parser.formatter.format_description = lambda description: description

    opts, args = parser.parse_args()

    # Set up clean logging to stderr
    log_levels = [logging.CRITICAL, logging.ERROR, logging.WARNING,
                  logging.INFO, logging.DEBUG]
    opts.verbose = min(opts.verbose - opts.quiet, len(log_levels) - 1)
    opts.verbose = max(opts.verbose, 0)
    logging.basicConfig(level=log_levels[opts.verbose],
                        format='%(levelname)s: %(message)s')


class Video():
    """ Parent class """

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """ This class builds a movie website """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, duration, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """ This class builds a movie website """

    def __init__(self, title, duration, tvshow_storyline, poster_image, trailer_youtube):
        Video.__init__(self, title, duration)
        self.storyline = tvshow_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
