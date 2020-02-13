
class Node():

	def __init__(self, alphabet):

		self.char = alphabet
		self.children = []
		self.end_of_word = False
		self.counter = 1
'''
Create a tree of alphabets like this:
	
			 +
			/ \
		   c   d
		  /		\
		 a       o
		/  \	  \
	   t   p	   g

'''
class Trie():

	def __init__(self):

		self.root = Node('+')

	def addWord(self, word):

		node = self.root

		# found_flag = False

		for letter in word:

			found_flag = False

			for child in node.children:


				if child.char == letter:
					child.counter += 1
					node = child
					found_flag = True
					break

			if not found_flag:

				newChild = Node(letter)
				node.children.append(newChild)
				node = newChild

		node.end_of_word  = True

	def findWord(self, word):

		node = self.root

		found_flag = False

		for letter in word:
			
			found_flag = False
			
			for child in node.children:

				if child.char == letter:
					node = child
					found_flag = True
					break

		return found_flag and node.end_of_word

	def delWord(self, word):

		node = self.root
		

		for letter in word:
			for child in node.children:

				if child.char == letter:
					
					if child.counter == 1:

						node.children.remove(child)
						return
					else:

						node = child
						break
		

		#In the case we want to delete 'dog' but keep 'dogs'
		if letter == node.char:

			node.end_of_word = False
			return

		
		print("Word not found")		
		return

	def discover(self, node, prefix):

		words = []

		for child in node.children:

			if child.end_of_word:
				words.append(prefix + child.char)

				if child.children:
					words.extend(self.discover(child, prefix + child.char))
			else:
				words.extend(self.discover(child, prefix + child.char))

		return words



	def wordsWithPrefix(self, prefix):

		node = self.root
		found_flag = False
		
		for letter in prefix:
			
			found_flag = False

			for child in node.children:
				
				if letter == child.char:
					node = child
					found_flag = True
					break


			if not found_flag:
				return []
		
		return self.discover(node, prefix)

	def allWords(self):

		node = self.root

		return self.discover(node, "")






