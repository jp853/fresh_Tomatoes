import webbrowser

class Movie():
    """ This class provides a way to store movie related information """
    VALID_RATINGS = ["G","PG","PG-13","R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, year, rating):
        """ This __init__ function constructor uses 'self' as the instance in question. So,
            when a movie instance is called, 'self' refers the instance variables to
            the movie instance called and/or the instance method called. """

        #instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year
        self.rating = rating

    def show_trailer(self):
        """ This method launches the youtube trailer """
        webbrowser.open(self.trailer_youtube_url)
