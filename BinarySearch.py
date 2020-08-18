def BinarySearch(int_list, target):
	low = 0
	high = len(int_list)-1
	
	while (low<= high):
		mid = (low+high)//2
		if (int_list[mid]==target):
			return mid
		elif(int_list[mid]>target):
			high = mid-1
		elif(int_list[mid]<target):
			low = mid+1

	return None

int_list = [1,2,7,10,12,17,20,23,24,28]
target = 1
print(BinarySearch(int_list, target))

