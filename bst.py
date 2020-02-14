

class Node():

	def __init__(self, value):

		self.value = value
		self.left = None
		self.right = None


class BinarySearchTree():

	def __init__(self):

		self.root = None

	def addUtil(self, node, value):

		if node == None:

			node = Node(value)
			return node

		elif node.value > value:

			if node.left == None:
				node.left = Node(value)
				return node
			
			else:
				return self.addUtil(node.left, value)

		elif node.value < value:
			if node.right == None:
				node.right = Node(value)

			else:	
				return self.addUtil(node.right, value)
		else:
			print("The value {} exists in Binary Search Tree".format(value))


	def add(self, value):

		if self.root == None:

			self.root = Node(value)

		else:

			return self.addUtil(self.root, value)



	def findUtil(self, node, value):

		if node == None:

			return False

		elif node.value == value:

			return True

		elif node.value > value:

			return self.findUtil(node.left, value)

		else:

			return self.findUtil(node.right, value)


	def find(self, value):

		if self.root == None:
			return False

		else:

			return self.findUtil(self.root, value)


	def inorderUtil(self, node):

		if node:
			self.inorderUtil(node.left)
			print(node.value)
			self.inorderUtil(node.right)

	def inorderTrans(self):

		if self.root:

			self.inorderUtil(self.root)

		else:
			print("Empty Tree")

	def printLeafsUtil(self, node):

		if not node:
			return

		if node.left == None and node.right == None:
			print(node.value)
			return

		self.printLeafsUtil(node.left)
		self.printLeafsUtil(node.right)

	def printLeafs(self):

		if self.root and self.root.left == None and self.root.right == None:

			print(self.root.value)

		else:
			self.printLeafsUtil(self.root)



b = BinarySearchTree()

b.add(1)
b.add(2)
b.add(20)
b.add(-1)
b.add(0)
b.add(-2)
b.add(-2)
# b.inorderTrans()
b.printLeafs()