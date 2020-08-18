def merge_list(my_list, her_list):

	merged_list_size = len(my_list) + len(her_list)
	merged_list = [None] * merged_list_size

	my_list_index = 0
	her_list_index = 0
	merged_list_index = 0

	my_list_length = len(my_list)
	her_list_length = len(her_list)

	while my_list_index < len(my_list) and my_list_length > 0 and her_list_length > 0:
		if my_list[my_list_index] < her_list[her_list_index]:
			merged_list[merged_list_index] = my_list[my_list_index]
			my_list_index += 1
			merged_list_index += 1
			my_list_length -= 1
		else:
			merged_list[merged_list_index] = her_list[her_list_index]
			her_list_index += 1
			merged_list_index += 1
			her_list_length -= 1

	if my_list_length == 0:
		while merged_list_index < len(merged_list):
			merged_list[merged_list_index] = her_list[her_list_index]
			her_list_index += 1
			merged_list_index += 1
			her_list_length -= 1
	elif her_list_length == 0:
		while merged_list_index < len(merged_list):
			merged_list[merged_list_index] = my_list[my_list_index]
			my_list_index += 1
			merged_list_index += 1
			my_list_length -= 1
			
	return merged_list 

my_list = [1,3,5,7,9,11]
her_list = [12,13,14,15,16,17]
result = merge_list(my_list, her_list)
print(result)