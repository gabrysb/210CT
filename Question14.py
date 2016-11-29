def DFS(self, vertex):
    """docstring"""
   	s = []
    	seen = []
    	s.push(vertex)
    	while s != False:  #checks if stack is empty
      		u = s.pop()
      		if u not in seen:
        			seen.append(u)
        			for val in range(0, len(self.graph)-1):  #seaches for value val
          				if val == u:
            				temp = self.graph[val]  #takes all values from e (array)
            				for e in temp:
              					s.push(e)  #pushes all array values into stack
    	return (seen)


  def BFS(self, vertex):
    	q = []
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
