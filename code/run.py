# Author: Md Lutfar Rahman, PhD student, UofM
# Recommendation system
from DataReader import *
from CollabFilter import *

print "Started ...\n"
ratings_file = '../netflix/ratings.txt'
movie_titles_file = '../netflix/movie_titles.txt'

ratings,avg_ratings,movies,seen_movies = DataReader(ratings_file,movie_titles_file).load()
Algo = CollabFilter(ratings,avg_ratings,movies,seen_movies)


#user_id = 940016
user_id = int(input("Enter an user_id: "))
#K = 12
K = int(input("Number of movies to recommend: "))
print('\n')
Algo.get_movie_suggestion(user_id,K)

print "\nEnded..."

