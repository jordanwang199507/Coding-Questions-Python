def sort_score (unsorted_scores, Highest_possible_score):
	
	score_counts = {}
	sorted_score = []
	score = 0

	for i in unsorted_scores:
		if i in score_counts:
			score_counts[i] += 1
		else:
			score_counts[i] = 1

	for i in range (0, Highest_possible_score+1):
		if i in score_counts and score_counts[i]>1:
			sorted_score.append(i)
			while score_counts[i]!=1:
				score_counts[i]-=1
				sorted_score.append(i)
		elif i in score_counts and score_counts[i]==1:
			sorted_score.append(i)

	print(sorted_score)



unsorted_scores = [45,45,23,88,12,74,100,23,23,23,45,45,45,0]
Highest_possible_score = 100
sort_score(unsorted_scores, Highest_possible_score)