L = [1,2,3,4,1,5,1,6,7]


def subseq ():
temp = [ ]
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
				temp = [ ]
     		 	else:
        				count = 0
				temp = [ ]
  	return (big, arr)


x = subseq()
print(x)
