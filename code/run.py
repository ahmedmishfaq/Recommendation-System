# Author: Md Lutfar Rahman, PhD student, UofM
# Recommendation system
from DataReader import *
from CollabFilter import *

print "Starting"
ratings_file = '../netflix/ratings.txt'
movie_titles_file = '../netflix/movie_titles.txt'

ratings,avg_ratings,movies,seen_movies = DataReader(ratings_file,movie_titles_file).load()
result = CollabFilter(ratings,avg_ratings,movies,seen_movies)

common = result.get_pearson_coeficient(1392773,998229)
unrated = result.get_unrated_movies(998229)
p = result.get_movie_rating_prediction(998229,17137)
s = result.get_movie_suggestion(864172,11)

print p
print "end"

