class Node:
	def __init__(self, key):
		self.value = key
		self.left = None
		self.right = None

def find_2nd_largest_item(root, size):
	if (size == 2):
		return root
	elif (size < 2):
		return "Error: no second largest item"

	if (root.right != None):
		cur = root
		while (cur.right != None):
			prev = cur
			cur = cur.right
			if ((cur.right == None) and (cur.left!=None)):
				prev = cur
				cur = cur.left
				while (cur.right!= None):
					prev = cur
					cur = cur.right
				return cur.value
		return prev.value
	else:
		cur = root.left
		while (cur.right != None):
			cur = cur.right
		return cur.value




root = Node(5)
node1 = Node(3)
node2 = Node(8)
root.left = node1
root.right = node2
node3 = Node(1)
node4 = Node(4)
node1.left = node3
node1.right = node4
node5 = Node(7)
node6 = Node(13)
node2.left = node5
node2.right = node6
node7 = Node(10)
node6.left = node7
node8 = Node(9)
node9 = Node(11)
node7.left = node8
node7.right = node9
#node10 = Node(12)
#node9.right = node10
size = 11
print(find_2nd_largest_item(root,size))

root = Node(20)
node1 = Node(25)
node2 = Node(18)
root.right = node1
root.left = node2
node3 = Node(19)
node4 = Node(14)
node2.right = node3
node2.left = node4
node5 = Node(30)
node6 = Node(21)
node1.right = node5
node1.left = node6
node7 = Node(32)
node8 = Node(28)
node5.right = node7
node5.leftr = node8
size = 9
print(find_2nd_largest_item(root, size))

