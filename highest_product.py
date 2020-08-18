def highest_product(list_intergers):

	if len(list_intergers) < 3:
		print("Error")
		return 

	highest_product_3 = list_intergers[0]*list_intergers[1]*list_intergers[2]
	highest_product_2 = list_intergers[0]*list_intergers[1]
	highest = max(list_intergers[0], list_intergers[1])
	lowest_product_2 = list_intergers[0]*list_intergers[1]
	lowest = min(list_intergers[0],list_intergers[1])

	for i in range(2,(len(list_intergers))):
		current = list_intergers[i]
		highest_product_3 = max(highest_product_3, current*highest_product_2, current*lowest_product_2)
		highest_product_2 = max(highest_product_2, current*highest, current*lowest)
		lowest_product_2 = min(lowest_product_2, current*highest, current*lowest)
		highest = max(highest, current)
		lowest = min(lowest, current)
	return highest_product_3


list_intergers = [2, 5, 9, -4, -12,0,-5]
print(highest_product(list_intergers))
