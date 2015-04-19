#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Builds the html page containing the Movie Trailer
Website using data coming from entertainment_center.py.
"""

__appname__ = "Trailer Website"
__author__ = "Davide Nastri"
__version__ = "0.1beta"
__license__ = "GNU GPL 3.0"

import webbrowser
import os
import re

# The main page layout and title bar
MAIN_PAGE_CONTENT = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
        <nav class="navbar navbar-default navbar-fixed-top">
            <div class="container-fluid">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <span class="navbar-brand">Pre-Popcorn Time <em title="Nerd Edition">N.E.</em></span>
                </div>
                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav navbar-right">
                        <li class="active text-center"><a id="btn-movies" href="#movies"><span class="glyphicon glyphicon-film"></span><br>Movies</a></li>
                        <li class="text-center"><a id="btn-tvshows" href="#tvshows"><img src="http://1.bp.blogspot.com/-wkX5QCI9_JA/UxkheItkXLI/AAAAAAAAEks/luP9qjuXkyw/s1600/House-and-Appliances-Tv-icon.png" width="16px" /><br>Tv Shows</a></li>
                        <li class="text-center"><a id="btn-about" href="#about"><span class="glyphicon glyphicon-info-sign"></span><br>About</a></li>
                    </ul>
                </div>
                <!-- /.navbar-collapse -->
            </div>
            <!-- /.container-fluid -->
        </nav>
    </div>

    <div id="movies-container" class="container content">
    <h2>Movie Trailers</h2>
    <p>Click on any movie to see its trailer</p>
      {movie_tiles}
    </div>
    <div id="tvshows-container" class="container content" hidden>
    <h2>Tv Shows Trailers</h2>
    <p>Click on any tv show to see its trailer</p>
      {tvshow_tiles}
    </div>
    <div id="about-container" class="container content" hidden>
        <h2>About me</h2>
        <img title="Ah, datetime flies..." class="center-block" src="https://dl.dropboxusercontent.com/u/3948090/pitto-sedici-bit.jpg" />
        <p class="text-center"><small>This is a picture of me when I was just 8-bit old</small></p>
        <p>My name is <span title="Tah dah!">Davide Nastri</span> and I am a proud full time <span title="Let's say it: geeks are simply overrated">nerd</span>.</p>
        <p>Here's <span title="3">three</span> things I consider better than <span title="Yummy :D">N<span class="text-danger">utella</span></span>:</p>
        <ul>
            <li>
                Python
            </li>
            <li>
                Web Development
            </li>
            <li>
                IoT
            </li>
        </ul>
        <br>
        <p>Want to know more?</p>
        <p>Check my
            <a title="Click me! Click!" href="https://it.linkedin.com/in/davidenastri">
                <img style="margin-bottom: 2px;" src="https://static.licdn.com/scds/common/u/img/webpromo/btn_profile_bluetxt_80x15.png" width="80" height="15" border="0" alt="View Davide Nastri's profile on LinkedIn">
            </a>!
        </p>
    </div>
  </body>
</html>
'''

# Styles and scripting for the page
MAIN_PAGE_HEAD = '''
<head>
    <meta charset="utf-8">
    <title>Pre-Popcorn Time</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">

    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

    <style type="text/css" media="screen">
    body {
        padding-top: 80px;
    }

    #trailer .modal-dialog {
        margin-top: 200px;
        width: 640px;
        height: 480px;
    }

    .hanging-close {
        position: absolute;
        top: -12px;
        right: -12px;
        z-index: 9001;
    }

    #trailer-video {
        width: 100%;
        height: 100%;
    }

    .movie-tile {
        margin-bottom: 20px;
        padding-top: 20px;
    }

    .movie-tile:hover {
        background-color: #EEE;
        cursor: pointer;
    }

    .tvshow-tile {
        margin-bottom: 20px;
        padding-top: 20px;
    }

    .tvshow-tile:hover {
        background-color: #EEE;
        cursor: pointer;
    }

    .scale-media {
        padding-bottom: 56.25%;
        position: relative;
    }

    .scale-media iframe {
        border: none;
        height: 100%;
        position: absolute;
        width: 100%;
        left: 0;
        top: 0;
        background-color: white;
    }
    </style>
    <script type="text/javascript" charset="utf-8">
    // Pause the video when the modal is closed
    $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function(event) {
        // Remove the src so the player itself gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        $("#trailer-video-container").empty();
    });
    // Start playing the movie whenever the trailer modal is opened
    $(document).on('click', '.movie-tile', function(event) {
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
        var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
        $("#trailer-video-container").empty().append($("<iframe></iframe>", {
            'id': 'trailer-video',
            'type': 'text-html',
            'src': sourceUrl,
            'frameborder': 0
        }));
    });

    // Start playing the tvshow whenever the trailer modal is opened
    $(document).on('click', '.tvshow-tile', function(event) {
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
        var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
        $("#trailer-video-container").empty().append($("<iframe></iframe>", {
            'id': 'trailer-video',
            'type': 'text-html',
            'src': sourceUrl,
            'frameborder': 0
        }));
    });


    // Show movies
    $(document).on('click', '#btn-movies', function() {
        if ( $(this).parent().hasClass('active') ) {
            // do nothing
        } else {
            $('.content').slideUp();
            $('#movies-container').slideDown();
            $("#btn-movies").parent().addClass('active');
            $("#btn-tvshows").parent().removeClass('active');
            $("#btn-about").parent().removeClass('active');
        }
    });

    // Show tvshows
    $(document).on('click', '#btn-tvshows', function() {
        if ( $(this).parent().hasClass('active') ) {
            // do nothing
        } else {
            $('.content').slideUp();
            $('#tvshows-container').slideDown();
            $("#btn-movies").parent().removeClass('active');
            $("#btn-tvshows").parent().addClass('active');
            $("#btn-about").parent().removeClass('active');
        }
    });

    // Show about
    $(document).on('click', '#btn-about', function() {
        if ( $(this).parent().hasClass('active') ) {
            // do nothing
        } else {
            $('.content').slideUp();
            $('#about-container').slideDown();
            $("#btn-movies").parent().removeClass('active');
            $("#btn-tvshows").parent().removeClass('active');
            $("#btn-about").parent().addClass('active');
            }
    });


    // Animate in the movies when the page loads
    $(document).ready(function() {
        $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
        });
    });
    </script>
</head>
'''


# A single movie entry html template
MAIN_TITLE_CONTENT_MOVIE = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img title="Duration: {duration} minutes
Storyline: {storyline}" src="{poster_image_url}" width="220" height="342">
    <h2>{title}</h2>
</div>
'''

# A single tvshow entry html template
MAIN_TITLE_CONTENT_TVSHOW = '''
<div class="col-md-6 col-lg-4 tvshow-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img title="Number of seasons: {seasons}
Storyline: {storyline}" src="{poster_image_url}" width="220" height="342">
    <h2>{title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    """ The HTML content for this section of the page
    """
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match \
                           or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += MAIN_TITLE_CONTENT_MOVIE.format(
            title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            duration=movie.duration,
            storyline=movie.movie_storyline
        )
    return content


def create_tvshow_tiles_content(tvshows):
    """ The HTML content for this section of the page
    """
    content = ''
    for tvshow in tvshows:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', tvshow.trailer_youtube_url)
        youtube_id_match = youtube_id_match \
                           or re.search(r'(?<=be/)[^&#]+', tvshow.trailer_youtube_url)
        print youtube_id_match
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the tvshow with its content filled in
        content += MAIN_TITLE_CONTENT_TVSHOW.format(
            title=tvshow.title,
            poster_image_url=tvshow.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            seasons=tvshow.seasons,
            storyline=tvshow.movie_storyline
        )
    return content


def open_page(movies, tvshows):
    """ Create or overwrite the html output file
    """
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = MAIN_PAGE_CONTENT.format(
        movie_tiles=create_movie_tiles_content(movies),
        tvshow_tiles=create_tvshow_tiles_content(tvshows)
    )
    print create_tvshow_tiles_content(tvshows)
    # Output the file
    output_file.write(MAIN_PAGE_HEAD + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible
    