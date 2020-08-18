def check_length (flight_length, movie_length):
	
	dictionary = dict()
	num_movies = len(movie_length)
	index = 0

	while index < num_movies:
		second_movie = flight_length - movie_length[index]
		if second_movie in dictionary:
			return True
		else:
			dictionary[movie_length[index]] = index
			index += 1
	return False


#test
flight_length = 100
movie_length = [80, 30, 45, 20, 75]
result = check_length(flight_length, movie_length)
print(result)


flight_length = 200
movie_length = [100, 20, 120, 30, 70]
result = check_length(flight_length, movie_length)
print(result)
