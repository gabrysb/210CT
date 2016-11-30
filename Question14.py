""" Implement BFS and DFS traversals for the above graph. Save the nodes traversed in sequence to a text file."""

 def DFS(self, vertex):
   """ Uses a stack so it goes all the way down a branch and stores the values that can then be popped once the nodes have all been found. This particular DFS is done pre-order."""
  	s = []       #stack
   	seen = []
   	s.push(vertex)
   	while s != False: 
     		u = s.pop()
     		if u not in seen:
       		seen.append(u)
       		for val in range(0, len(self.graph)-1): 
         			if val == u:
           			temp = self.graph[val]  #takes all values from e (array)
           			for e in temp:
             				s.push(e) 
   	return (seen)

 def BFS(self, vertex):
     """Uses a queue for a FIFO approach. This method goes through each edge from the first node, and then moves down the graph to get all the edges of the next node."""
   	q = []     #queue
   	seen = []
   	q.enqueue(vertex)
   	while q != False:
     		u = q.dequeue()
     		if u not in seen:
       		seen.append(u)
       		for val in range(0, len(self.graph)-1):
         			if val == u:
	temp = self.graph[val]  #takes all values from e (array)
           			for e in temp:
             				q.enqueue(e)
