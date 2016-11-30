""" Given a sequence of n integer numbers, extract the sub-sequence of maximum length which is in ascending order."""

L = [1,2,3,4,1,5,1,6,7]

def subseq ():
 	"""This function runs through the list and if it hits a value where the next value is lower, then it saves the previous values and the length of the sub-list, and clears those temp values and carries on iterating until it hits the end of the list."""
temp = []
 	count = 0
 	big= 0
	for i in range(1, len(L)-1):
  		if L[i] >= L[i-1]:
    			count =+1
			temp.append(L[i])
   		elif L[i] < L[i-1]:
     			if count > big:
      			big = count
       			count = 0
				arr = temp
				temp = []
    		 	else:
       			count = 0
				temp = []
 	return (big, arr)

x = subseq()
print(x)
