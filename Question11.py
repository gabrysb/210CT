def delete(self,x):
  	if x.prev != None:
    		x.prev.next = x.next
  	else:
    		self.head = x.next
  	if x.next != None:
    		x.next.prev = x.prev
  	else:
    		self.tail = x.prev
