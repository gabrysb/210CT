def in_order(root):
  	curr = root
  	stk = []
  	run = True
  	while run = True:
    		if curr != None:
      			stk.append(curr)
      			curr = curr.left
    		else:
      			if stk != false:
        				temp = stk.pop()
        				print(temp)
        				curr = curr.right
        
def tree_sort(arr):
  	for i in range(0, len(arr)-1):
    		tree_insert(Tree, i)
    		in_order(Tree)
