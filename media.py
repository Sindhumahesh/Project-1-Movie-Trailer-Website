import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline,poster_image, trailer_youtube,movie_language):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movielanguage = movie_language

#__init__ is called immediately after an instance of the class is created.
#__init__ initiliazes or creates space in memory
#self is the instance being created
