from Stack_Mod import Stack

class Queue():
	def __init__(self):
		self.InStack = Stack()
		self.OutStack = Stack()

	def Enqueue(self, item):
		self.InStack.push(item)

	def Dequeue(self):
		if self.OutStack.peek()!=None:
			return self.OutStack.pop()
		elif self.InStack.peek() == None:
			return None
		else:
			while self.InStack.peek()!=None:
				item = self.InStack.pop()
				self.OutStack.push(item)

			return self.OutStack.pop()

StackQueue = Queue()
StackQueue.Enqueue(1)
StackQueue.Enqueue(2)
StackQueue.Enqueue(3)
StackQueue.Enqueue(4)
print(StackQueue.Dequeue())
StackQueue.Enqueue(5)
StackQueue.Enqueue(6)
print(StackQueue.Dequeue())
print(StackQueue.Dequeue())
print(StackQueue.Dequeue())
print(StackQueue.Dequeue())

