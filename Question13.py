CLASS GRAPH
	graph <- {}


	ADD_VERTEX(self, vertex)
		IF vertex is not in self.graph
			vertex <- [ ]
	
	ADD_EDGES(self, edge, vertex)
		FOR vertex, i in self.graph
			IF i = vertex
				APPEND edge to self.edges[vertex]




class Graph():
  	def __init__(self):
    		self.graph={ }   #store vertices in dictionary with the keys being the vertices and the values being the edges - {"a": [b,c], "b": [a], "c": [a]} etc
    
  	def AddVertex(self, vertex):
    		if vertex not in self.graph:
      			self.graph[vertex] = []
      
  	def AddEdge(self, edge, vertex):
    		for i in self.graph:
      			if i == vertex:
        				self.edges[vertex].append(edge)
  
