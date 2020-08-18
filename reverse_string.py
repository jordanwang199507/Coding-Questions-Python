def reverse(array):

	left_index = 0
	right_index = len(array)-1

	while left_index < right_index:
		temp = array[left_index]
		array[left_index] = array[right_index]
		array[right_index]=temp
		left_index= left_index+1
		right_index=right_index-1


str1 = ['e','c','a','l','p','n','i']
reverse(str1)
print (str1)
