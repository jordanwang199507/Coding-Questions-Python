from Stack_Mod import Stack

class LargestStack():

	def __init__(self):
		self.stack = Stack()
		self.max = Stack()

	def push(self, item):
		self.stack.push(item)

		if self.max.peek()==None:
			self.max.push(item)
		elif item >= self.max.peek():
			self.max.push(item)

	def pop(self):
		item = self.stack.pop()

		if item == None:
			return None
		elif item == self.max.peek():
			self.max.pop()

	def peek(self):
		return self.stack.peek()

	def getMax(self):
		return self.max.peek()

stack = LargestStack()
stack.push(10)
stack.push(9)
stack.push(15)
stack.push(20)
stack.push(8)
print (stack.getMax())
stack.pop()
stack.pop()
print(stack.getMax())
print(stack.peek())