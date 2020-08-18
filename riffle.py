def is_single_riffle(shuffled_deck, half1, half2):

	shuffled_deck_index = 0
	half1_index = 0
	half2_index = 0

	while shuffled_deck_index < len(shuffled_deck):

		if ((half1_index < len(half1)) and half1[half1_index]==shuffled_deck[shuffled_deck_index]):
			half1_index = half1_index + 1
			shuffled_deck_index = shuffled_deck_index + 1

		elif ((half2_index < len(half2)) and half2[half2_index]==shuffled_deck[shuffled_deck_index]):
			half2_index = half2_index + 1
			shuffled_deck_index = shuffled_deck_index + 1

		else: 
			return False

	return True

#test 1
shuffled_deck = [3,12,2,20,8,52,1,38,26,41]
half1 = [3,20,8,1,26]
half2 = [12,2,52,38,41]
print(is_single_riffle(shuffled_deck, half1, half2))

#test 2
shuffled_deck = [3,12,2,20,8,52,1,38,26,41]
half1 = [3,12,2,20,8]
half2 = [52,1,38,26,41]
print(is_single_riffle(shuffled_deck, half1, half2))

#test 3
shuffled_deck = [3,12,2,20,8,52,1,38,26,41]
half1 = [3,12,2,44,8]
half2 = [52,1,38,26,41]
print(is_single_riffle(shuffled_deck, half1, half2))