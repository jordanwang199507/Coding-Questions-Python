def match_parent(sentence, index):

	parent_count = 0

	for i in range(index+1, len(sentence)):
		
		char = sentence[i]

		if char == '(':
			parent_count = parent_count+1
		elif char ==')':
			if(parent_count == 0):
				return i
			else:
				parent_count = parent_count-1

	return 'No closing parenthesis'

#test
sentence = '(abc(def))'
print(match_parent(sentence,0))
sentence = '(abc(def)'
print(match_parent(sentence,0))