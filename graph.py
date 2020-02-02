from collections import defaultdict


class Graph(object):

	def __init__(self, connections, directed = False):

		self._graph = defaultdict(set)
		self.directed = directed
		self.add_connections(connections)

	def add_connections(self, connections):

		for node1, node2 in connections:
			self.add(node1, node2)

	def add(self, node1, node2):

		if node2 not in self._graph[node1]:
			self._graph[node1].add(node2)

			if not self.directed:
				self._graph[node2].add(node1)

	def remove(self, node):

		for n, connections in self._graph.items():

			try:
			
				connections.remove(node)

			except KeyError:
				pass

		try:

			del self._graph[node]
		
		except KeyError:
			pass

	def is_connected(self, node1, node2):

		return node1 in self._graph[node2] and node2 in self._graph[node1]


	def __str__(self):
		
		return '{}({})'.format(self.__class__.__name__, dict(self._graph))



# connections = [(1, 2), (2, 3), (2, 4),(3, 4), (5, 6), (6, 3)]

# g = Graph(connections = connections, directed = False)
# g.add(5,6)
# print(g._graph)