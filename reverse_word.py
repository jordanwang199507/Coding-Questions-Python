def reverse_word(message):

	left_index = 0
	right_index = len(message)-1

	while left_index < right_index:
		temp = message[left_index]
		message[left_index] = message[right_index]
		message[right_index] = temp
		left_index = left_index + 1
		right_index = right_index - 1

	message_length = len(message)
	end = 0
	start = 0

	while end < message_length:
		if end == message_length - 1:
			reverse(message, start, end)
			end = end + 1
		elif message[end] != ' ':
			end = end + 1
		else:
			reverse(message, start, end - 1)
			start = end + 1
			end = end + 1

def reverse(message, start, end):
	while start<end:
		temp = message[start]
		message[start] = message[end]
		message[end] = temp
		end = end - 1
		start = start + 1

message = ['w','o','r','d','s',' ','s','o','m','e',' ','r','e','v','e','r','s','e']
reverse_word(message)
print(message)