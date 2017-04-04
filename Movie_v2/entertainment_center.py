import fresh_tomatoes
import media

    #Movie Instances
the_empire_strikes_back = media.Movie("The Empire Strkies Back", #movie_title
                        "Luke Skywalker must learn to become" #movie_storyline
                        " a jedi knight",
                        "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg", #poster_image
                        "https://www.youtube.com/watch?v=JNwNXF9Y6kY", #trailer_youtube
                        1980, #year
                        "PG") #rating

avatar = media.Movie("Avatar", #movie_title
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", #poster_image
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY", #trailer_youtube
                     2009, #year
                     "PG-13") #rating

school_of_rock = media.Movie("School of Rock", #movie_title
                             "Using rock music to learn", #movie_storyline
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", #poster_image
                             "https://www.youtube.com/watch?v=3PsUJFEBC74", #trailer_youtube
                             2003, #year
                             "PG-13") #rating

cool_runnings = media.Movie("Cool Runnings", #movie_title
                          "Jamaca's first bobsled team", #movie_storyline
                          "https://upload.wikimedia.org/wikipedia/en/7/76/Coolrunnings.jpg", #poster_image
                          "https://www.youtube.com/watch?v=wLlmymHRNZg", #trailer_youtube
                          1993, #year
                          "PG") #rating

deadpool = media.Movie("Deadpool", #movie_title
                        "A merc with a mouth gets revenge", #movie_storyline
                        "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg", #poster_image
                        "https://www.youtube.com/watch?v=9vN6DHB6bJc", #trailer_youtube
                        2016, #year
                        "R") #rating

hunger_games = media.Movie("Hunger Games", #movie_title
                           "A really real reality show", #movie_storyline
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", #poster_image
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY", #trailer_youtube
                           2012, #year
                           "PG-13") #rating

#Pushes all movie instances into an array so it can be passed into an input
#to generate an html file and be opened into a browser
movies = [the_empire_strikes_back, avatar, school_of_rock, cool_runnings, deadpool, hunger_games]
# This function call uses list/array of movie instances as an input to generate a HTML file
# and open it in the browser.
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print (media.Movie.__init__.__doc__)
