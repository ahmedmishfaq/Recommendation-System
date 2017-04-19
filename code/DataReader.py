from csv import reader

class DataReader():

	def __init__(self,ratings_file,movie_titles_file):
		self.ratings_file = ratings_file
		self.movie_titles_file = movie_titles_file
		self.ratings = {}
		self.movies = {}
		self.avg_ratings = {}
		self.seen_movies = {}


	def load(self):
		with open(self.ratings_file, 'r') as file:
			csv_reader = reader(file)
			for row in csv_reader:
				if not row:
					continue
				self.setup_data(row)

		self.load_movies()
		return self.ratings,self.avg_ratings,self.movies,self.seen_movies

	def load_movies(self):
		with open(self.movie_titles_file, 'r') as file:
			csv_reader = reader(file)
			for row in csv_reader:
				if not row:
					continue
				movie_id = int(row[0].strip())
				self.movies[movie_id] = row[1],row[2]

		return self.movies


	def setup_data(self,row):

		movie_id = int(row[0].strip())
		user_id = int(row[1].strip())
		rating = float(row[2].strip())

		if user_id not in self.ratings:
			self.ratings[user_id] = {}
			self.avg_ratings[user_id] = 0,0
		self.ratings[user_id][movie_id] = rating

		self.setup_avg_rating(movie_id,user_id,rating)

		self.seen_movies[movie_id] = user_id,rating


	def setup_avg_rating(self,movie_id,user_id,rating):
		
		current_count = self.avg_ratings[user_id][0]
		current_avg = self.avg_ratings[user_id][1]
		
		new_count = current_count + 1
		new_avg = (current_count*current_avg + rating)/new_count

		self.avg_ratings[user_id] = new_count, new_avg
