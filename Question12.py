class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
  
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print tree.value
 
 
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print tree.value
    if(tree.right!=None):
        in_order(tree.right)
 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)

 """ Implement the TREE_SORT algorithm in a language of your choice, based on the template provided on Moodle, but make sure that the INORDER function is implemented iteratively, rather than recursively."""

def in_order(root):
      """The while loop replaces the recursive part of the previous version of this function. This way when the while loop is running the value from the end of the loop is passed back up, much like you pass new values through as an argument."""
 	curr = root
 	stk = []  #stack
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
      """docstring"""
 	for i in range(0, len(arr)-1):
   		tree_insert(Tree, i)
   		in_order(Tree)
