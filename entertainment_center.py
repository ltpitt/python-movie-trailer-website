import media
import fresh_tomatoes

the_matrix = media.Movie("The Matrix",
                         "150 minutes",
                         "The world isn't real. Or it is?",
                         "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

the_social_network = media.Movie("The Social Network",
                                 "121 minutes",
                                 "Programming is coolest thing out there",
                                 "http://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                                 "https://www.youtube.com/watch?v=lB95KLmpLR4")

tron_legacy = media.Movie("Tron Legacy",
                          "127 minutes",
                          "The son of a guy enters into a videogame with cool music and bikes",
                          "http://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg",
                          "https://www.youtube.com/watch?v=L9szn1QQfas")

movies = [the_matrix, the_social_network, tron_legacy]

fresh_tomatoes.open_movies_page(movies)