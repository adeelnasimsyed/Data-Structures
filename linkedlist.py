

class Node():

	def __init__(self, value):

		self.value = value
		self.nextNode = None


class LinkedList():

	def __init__(self):

		self.headNode = None


	def addStart(self, value):

		if self.headNode == None:
			self.headNode = Node(value)
			return

		else:
			temp = Node(value)
			temp.nextNode = self.headNode
			self.headNode = temp

	def addEnd(self, value):

		if self.headNode == None:
			self.headNode = Node(value)
			return

		else:

			node = self.headNode

			while(node.nextNode):

				node = node.nextNode

			node.nextNode = Node(value)

	def delNode(self, value):

		if self.headNode == None:
			print("Value not found")
			return

		else:

			node = self.headNode

			while(node):

				if(node.value == value):
					print("Deleted {}".format(node.value))
					previous.nextNode = node.nextNode
					return
				
				previous = node
				node = node.nextNode

			print("Value not found")

	def insNodeAfter(self, value, prevNode):

		if self.headNode == None:
			print("Value not found")
			return

		else:

			node = self.headNode

			while(node):

				if(node.value == prevNode):
					
					temp = Node(value)
					temp.nextNode = node.nextNode
					node.nextNode = temp
					return


				node = node.nextNode					

			print("Value not found")

	def insNodeBetween(self, value, prevNode, nextNode):

		if self.headNode == None:
			print("Value not found")
			return

		else:

			node = self.headNode

			while(node):

				if(node.value == prevNode and node.nextNode.value == nextNode):
					
					temp = Node(value)
					temp.nextNode = node.nextNode
					node.nextNode = temp
					return


				node = node.nextNode					

			print("Value not found")

	def revList(self):

		node = self.headNode
		prevNode = None

		while(node):

			next_node = node.nextNode
			node.nextNode = prevNode
			prevNode = node
			node = next_node

		self.headNode = prevNode


			


	def printList(self):

		if self.headNode == None:
			print("")

		else:

			node = self.headNode

			while(node):

				print(node.value)
				node = node.nextNode



l = LinkedList()
l.addStart(100)
l.addStart(10)
l.addStart(1)
l.addEnd(200)
l.addEnd(300)
# l.insNodeAfter(400,10)

l.printList()


print("now reverse list")

l.revList()
l.printList()
