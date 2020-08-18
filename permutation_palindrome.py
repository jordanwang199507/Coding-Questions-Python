def permutation_palindrome (input_str):
	input_str = input_str.replace(" ", "") 
	input_str = input_str.lower() 

	dictionary = dict()

	for i in input_str:
		if i in dictionary and dictionary[i]==False:
			dictionary[i] = True
		else: 
			dictionary[i] = False

	odd_number = 0

	for keyword, value in dictionary.items():
		#print(dictionary)
		if (value == False) and odd_number == 0:
			odd_number += 1
		elif (value == False) and odd_number > 0:
			return False

	return True

palin_perm = "taco obscat" 
print(permutation_palindrome(palin_perm))


