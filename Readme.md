# Movie trailer website

The Movie Trailer Website project consists of server-side code to store a list of movies titles, along with its respective box art imagery and movie trailer website. The data should be served as a web page allowing visitors to review the movies and watch the trailers.

# How to run the code

To use this project you must have python installed as well as the project files.

to install python follow the following instructions:
1. open this link https://www.python.org/downloads/ and click download python 2.7.14
2. after the file downloaded follow instructions to install it.
3. Open Start menu and search for 'IDLE (Python GUI)'
4. from Python shell click Ctrl+o and select `entertainment_center.py` and click open.
5. run the file and enjoy the trailers of my favorite movies.

## Modules:
It consists of 3 modules **entertainment_center.py** , **media.py** and **fresh_tomatoes.py**

### media.py
This module is storing the movies data like title, story , image and youtube url

##### Examples of code:
`def __init__(self , movie_title ,movie_story , movie_image , trailer_youtube_url1):        
        self.title = movie_title
        self.story = movie_story
        self.poster_image_url = movie_image
        self.trailer_youtube_url = trailer_youtube_url1`
The **__init__()** method takes all the needed attributes that will be presented on the website.

### entertainment_center.py

This module creates an instances of the movies , collect them in an array and passes them to **fresh_tomatoes.py**.

##### Examples of code:
`v_for_vendetta = media.Movie("V for Vendetta" ,
                         "In a future British tyranny, a shadowy freedom fighter, known only by the alias of V, plots to overthrow it with the help of a young woman." ,
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BYzllMjJkODAtYjMwMi00YmNhLWFhYzAtZjZjODg5YzEwOGUwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY999_CR0,0,679,999_AL_.jpg" ,
                         "https://www.youtube.com/watch?v=lSA7mAHolAw")`
That's an example of how to create a movie instance.

`movs = [v_for_vendetta,avatar,the_god_father,sherlouk_houlms,karate_kid,star_wars]`
and then collect all the instances in an array called **movs**

`fresh_tomatoes.open_movies_page(movs)`
then pass this array to **fresh_tomatoes.py** method called **open_movies_page()** that will open a web page and list your movies in it.
