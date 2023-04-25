Application 'film_recomendation.py' is provdied to calculate the best movie by its iscussability and uniqueness. For this script to work, you need to provide data with your movies in such way:

movies - [list with all movies]
similarities - [pairs of similar movies]
friends - [list with movies, that your friends watch]

To run this program, Python 3.10 or higher is required!!!

You can use this app in 2 different ways:
1. Via CLI
To run app, you have to provide type of file, where your data stores and filepath to it. Programm suports ".txt" and ".json" file format

film_recommendation.py filetype(text, json) filepath

You can run "film_recommendation.py --help" for more details

2. Use FilmRecommendation as module
In this case, you can manually read data from ".txt" and ".json", parse data directly to FilmRecommendation object on initialization, or use stdin to apply data into object.

from film_recommendation import FilmRecommendation as F
f = F()
f.read_from_text(filepath)
or
f.read_from_json(filepath)
or
f.read_from_input()
or
movies = ['Matrix', ...]
similarities = [[...]]
friends = [[...]]
f = F(movies, similarities, friends)
@@@
f.get_best_film()