class node:
	def __init__(self,data=None):
		self.data = data
		self.next = None

class linked_list:
	def __init__(self):
		self.head = node()

	def append(self,data):
		new_node = node(data)
		cur = self.head
		while cur.next!=None:
			cur = cur.next
		cur.next = new_node

	def append_head(self,data):
		new_node = node(data)
		cur = self.head
		if cur.next == None:
			print("Error: Empty Linked List")
			return
		temp_node = cur.next
		cur.next = new_node
		cur = cur.next
		cur.next = temp_node

	def length(self):
		cur = self.head
		total = 0
		while cur.next!= None:
			total = total + 1
			cur = cur.next
		return total

	def display(self):
		elements = []
		cur_node = self.head
		while cur_node.next != None:
			cur_node = cur_node.next
			elements.append(cur_node.data)
		print(elements)

	def get_data(self,index):
		if index >= self.length():
			print ("ERROR: Index Out of Range")
			return 
		cur_index = 0
		cur_node = self.head
		while cur_node.next!= None:
			cur_node = cur_node.next
			if cur_index==index:
				return cur_node.data
			cur_index= cur_index+1

	def get_index(self,data):
		cur_node = self.head
		cur_index = 0
		while cur_node.next!= None:
			cur_node = cur_node.next
			if cur_node.data == data:
				return cur_index
			cur_index = cur_index+1 
			if cur_index >= self.length():
				print("Error: No such Value")
				return

	def get_last_index (self):
		cur = self.head
		total = 0
		while cur.next != None:
			cur = cur.next
			total = total+1
		last_index = total-1
		return last_index

	def erase(self, index):
		if index>=self.length():
			print ("ERROR: Index Out of Range")
			return
		cur_index = 0
		cur_node = self.head
		while cur_node!= None:
			last_node = cur_node
			cur_node = cur_node.next
			if cur_index == index:
				last_node.next = cur_node.next
				return
			cur_index = cur_index + 1

my_list = linked_list()

my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
print()
#number = input("Enter index number: ")
#print("element at index %d = %s" %(int(number), my_list.get(int(number)) ) ) 
#my_list.erase(3)
#my_list.display()

my_list.append_head(5)
my_list.append_head(10)
my_list.display()