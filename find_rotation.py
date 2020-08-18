def find_rotation (rotate_list):
	target = rotate_list[0]
	low = 0
	high = len(rotate_list)-1

	while (low < high):
		middle = (low + high)//2
		if (rotate_list[middle] >= target):
			low = middle
		elif (rotate_list[middle] < target):
			high = middle

		if low+1 == high:
			return high

rotate_list = [600, 700, 200, 300, 400]
print(find_rotation(rotate_list))

rotate_list = [600, 700, 800, 200, 400]
print(find_rotation(rotate_list))