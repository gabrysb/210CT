class Graph(object):
  """Modified to store weights as tuples in the dictionary."""

  def __init__(self):
    """Store vertices in dictionary with the keys being the vertices and the values being the edges - {"a": [(b,4),(c,3)], "b": [(a,4)], "c": [(a,3)]}."""
    self.graph={}   #
    
  def AddVertex(self, vertex):
    """ Checks for the vertex’s existence and adds in the argument as a key if it’s not already a vertex. """
    if vertex not in self.graph:
      self.edges[vertex] = {}
      
  def AddEdge(self, edge, vertex, weight):
    """ Finds the vertex in the dictionary and if it exists, the edge is added to the list stored as a value. Currently only adds edges in one direction. Modified to insert as tuples with both edge and weight."""
    for i in self.graph:
      if i == vertex:
        self.graph[vertex].update((vertex, weight))

def Dijkstras(self, start, end):
     """All vertices get a tentative weight of infinity and the starting node is set to 0. We then go through all the neighbours and use the distances in the graph to set the tentative weights. After we check the first neighbours we go through the neighbours’ neighbours, carrying on until we reach the final vertex. Every vertex we check has its tw revised if it is smaller than the first time it was visited."""
   	v = start
   	for node in self.graph:
     		node.tw = math.inf
   	start.tw = 0
   	seen = []
   	while v != end:
     		for u in self.graph[v]:
       			if v.tw + v[u][1] < u.tw:
         				u.tw = v.tw + v[u][1]
         				u.prev = v
       		seen.append(v)
       	minimum = math.inf
       	for n in self.graph:
         		if n not in seen and n.tw < min:
           		v = n
           		minimum = n.tw
