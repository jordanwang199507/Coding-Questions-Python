import random 
def random_number(floor, ceiling):
	return random.randrange(floor, ceiling)

def inplace_shuffle(the_list):
	if len(the_list)<=1:
		return the_list

	for i in range(0, len(the_list)-1):
		random = random_number(i, len(the_list)-1)

		if random != i:
			temp = the_list[random]
			the_list[random]=the_list[i]
			the_list[i] = temp
	return the_list

the_list = ['a','b','c','d']
print(inplace_shuffle(the_list))

