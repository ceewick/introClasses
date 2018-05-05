## Things for class movie to remember:
## Title; Storyline; poster_image; trailer_youtube
import webbrowser

class Movie():
    ''' Class provides a way to store movie related info'''
    VALID_RATINGS = ['G','PG','PG-13','R','NC-17']
    ## Class Variable ^^ same choices for all instance of class. All objects share constant list.
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        ## FIRST: instance.variable (?attribute?), 
        ## SECOND = argument for variable to be init
        
        ## Instance Method = function in class
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
    def show_poster(self):
        webbrowser.open(self.poster_image_url)

## Notes:
## Should define classes in one file, call classes in another file
## Classes typicall start in Cap
        
## Class variables in ALL CAPS        
## All classes come w/ come predef class variables: https://www2.lib.uchicago.edu/keith/courses/python/class/5/
        ## __doc__ = prints documentation on class. Via '''
        
## Inheritance:
    ## class Parent:
    ## --last_name
    ## --eye color
    ## class Child(inherents from parent)
    ## --number of toys    