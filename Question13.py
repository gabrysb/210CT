"""CLASS GRAPH
	graph <- {}

	ADD_VERTEX(self, vertex)
		IF vertex is not in self.graph
			vertex <- [ ]
	
	ADD_EDGES(self, edge, vertex)
		FOR vertex, i in self.graph
			IF i = vertex
				APPEND edge to self.edges[vertex]
"""
class Graph():
     """The graph class initialises as a dictionary that is filled with the vertices as the keys, and edges as values in a list."""

 	def __init__(self):
           """Initialises the graph as a dictionary. Stores vertices in dictionary with the keys being the vertices and the values being the edges - {"a": [b,c], "b": [a], "c": [a]}. """
   		self.graph={}   

 	def AddVertex(self, vertex):
           """Checks for the vertex’s existence and adds in the argument as a key if it’s not already a vertex."""
   		if vertex not in self.graph:
     			self.graph[vertex] = []
     
 	def AddEdge(self, edge, vertex):
           """Finds the vertex in the dictionary and if it exists, the edge is added to the list stored as a value. Currently only adds edges in one direction."""
   		for i in self.graph:
     			if i == vertex:
       			self.edges[vertex].append(edge)

if __name__ == '__main__':
	G = {}
	AddVertex(a)
	AddVertex(b)
	AddVertex(c)
	AddEdge(b,a)
	AddEdge(c,a)
	AddEdge(a,c)
	AddEdge(a,b)
