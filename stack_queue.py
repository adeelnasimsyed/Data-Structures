from collections import deque

#Last in, first out
class Stack():

	def __init__(self):

		self.stack = []

	def push(self, value):

		self.stack.append(value)

	def pop(self):

		return self.stack.pop()

	def peak(self):

		if (self.stack):
			return self.stack[-1]
		else:
			return []

	def __str__(self):

		return str(self.stack)

#First in, First out
class Queue():

	def __init__(self):

		self.queue = deque()

	def push(self, value):

		self.queue.append(value)

	def popFirst(self):

		self.queue.popleft()

	def popLast(self):

		self.queue.pop()

	def peakFirst(self):

		if (self.queue):
			return self.queue[0]
		else:
			return []

	def peakLast(self):

		if (self.queue):
			return self.queue[-1]
		else:
			return []

	def __str__(self):

		return str(self.queue)


