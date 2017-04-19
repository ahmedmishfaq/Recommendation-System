import math
import copy, random

class CollabFilter():

	def __init__(self,ratings,avg_ratings,movies,seen_movies):
		self.ratings = ratings
		self.rt_copy = copy.deepcopy(self.ratings)
		self.avg_ratings = avg_ratings
		self.movies = movies
		self.seen_movies = seen_movies


	def get_movie_suggestion(self,a,k):
		random_sample  = random.sample(self.get_unrated_movies(a),50)
		for j in random_sample:
			p = self.get_movie_rating_prediction(a,j)
			print p



	def get_movie_rating_prediction(self,a,j):
		
		if j in self.ratings[a]:
			print("Error! User already has a rating")
			return

		sum = 0
		normalizing_factor = 0.05

		for i in self.rt_copy:  # for all user
			if a!=i and j in self.rt_copy[i]:  # if user i has rated movie j
				w_ai = self.get_pearson_coeficient(a,i)
				v_ij = self.get_v_aj_minus_v_a(i,j)

				sum+=w_ai*v_ij

		return self.avg_ratings[a][1] + normalizing_factor*sum


	def get_unrated_movies(self,a):   # unrated movies at least seen by another user
		return set(self.seen_movies.keys()) - set(self.ratings[a].keys())



	def get_pearson_coeficient(self,a,i):   #calculate w(a,i)
		common_movies = self.get_commonly_voted_items(a,i)

		sum1 = 0
		sum2 = 0
		sum3 = 0
		for j in common_movies:
			diff_a = self.get_v_aj_minus_v_a(a,j)
			diff_i = self.get_v_aj_minus_v_a(i,j)

			sum1+=diff_a*diff_i
			sum2+=diff_a*diff_a
			sum3+=diff_i*diff_i

		if sum1 ==0 or sum2 ==0 or sum3==0:
			return 0
		return sum1/math.sqrt(sum2*sum3)


	def get_commonly_voted_items(self,a,i):    #user a and i both voted those items
		return set(self.ratings[a].keys()) & set(self.ratings[i].keys())
	
	def get_v_aj_minus_v_a(self,a,j):
		return self.ratings[a][j] - self.avg_ratings[a][1]