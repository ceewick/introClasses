import media
import fresh_tomatoes

toy_story = media.Movie('Toy_Story',
                        'A story of a boy and his toys',
                        'https://static.comicvine.com/uploads/original/12/126071/2427139-toy_story_1995.jpeg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc'
                        )

avatar = media.Movie('Avatar',
                     'Basically copy of Ferngully',
                     'http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY'
                     )

the_departed = media.Movie('The Departed',
                           'South Boston cop Billy Costigan (Leonardo DiCaprio) goes under cover to infiltrate the organization of gangland chief Frank Costello (Jack Nicholson).',
                           'https://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg',
                           'https://www.youtube.com/watch?v=SGWvwjZ0eDc'
                           )

gladiator = media.Movie('Gladiator',
                        'Movie of gladiator journey',
                        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqavktMm3pGd980S5nrI73fETFflNAVGra-6aWpNsathrWgxjOPYM0AA',
                        'https://www.youtube.com/watch?v=w5rVtxWTq8w'
                        )

movies = [toy_story,avatar,the_departed,gladiator]
fresh_tomatoes.open_movies_page(movies)
  
#print(toy_story.storyline)                        
#print(avatar.storyline)
#avatar.show_trailer()
#avatar.show_poster()
#print 'hello world'

## Class Docs
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__) 
#print(media.Movie.__dict__)

## Inheritance


## toy_story, avatar = instances of class -> objects
## instance variables=(movie_title, movie_storyline, poster_image, trailer_youtube)

