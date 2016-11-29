def Dijkstras(self, start, end):
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
