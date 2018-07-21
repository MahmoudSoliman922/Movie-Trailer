import webbrowser
# creating a class to hold movies information


class Movie():
    # defining the __data__ method that store the class documentation
    """This class provides a way to store movie related information"""
    # defining the __init__ method that hold the movies information arguments
    def __init__(self, movie_title, movie_story,
                 movie_image, trailer_youtube_url1):
        self.title = movie_title
        self.story = movie_story
        self.poster_image_url = movie_image
        self.trailer_youtube_url = trailer_youtube_url1
    # defining the method that opens the youtube trailer

    def show_trailer(self):
        webbrowser.open(self.youtubetrailer)
