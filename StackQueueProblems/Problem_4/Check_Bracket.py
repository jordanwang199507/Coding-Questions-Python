from Stack_Mod import Stack

def check_brackets(input_string):

	check_stack = Stack()

	for char in input_string:
		if char == '(' or char == '{' or char == '[':
			check_stack.push(char)
		elif char == ')':
			if check_stack.peek()!= '(':
				return False
			else:
				check_stack.pop()
		elif char == '}':
			if check_stack.peek()!= '{':
				return False
			else:
				check_stack.pop()
		elif char == ']':
			if check_stack.peek()!= '[':
				return False
			else:
				check_stack.pop()
	#return True if stack = None
	return check_stack.peek() == None

#test code
test0 = '{()[]}'
print(check_brackets(test0))
#True

test1 = '{[(])}'
print(check_brackets(test1))
#False