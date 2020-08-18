class node:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, value):
		if self.root == None:
			self.root = node(value)
		else:
			self._insert(value, self.root)

	def _insert(self, value, cur_node):
		if value < cur_node.value:
			if cur_node.left_child == None:
				cur_node.left_child = node(value)
			else: 
				self._insert(value, cur_node.left_child)