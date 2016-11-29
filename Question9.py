l <- [2,3,5,7,9,13] //global variable and so does not need to be called in the function parameters
low <- INPUT low
high <- INPUT high
left <- l[0]
right <- l[len(l)-1]


BINARY_SEARCH (left, right)
	IF left > right
		RETURN not found
	mid <- floor((right-left)/2)+left
	IF l[mid] < high AND l[mid] >low
		RETURN found
	ELSE IF l[mid] > high
		RETURN binary_search(left, mid-1)
	ELSE IF l[mid] < low
		RETURN binary_search(mid+1, right)


OUTPUT binary_search(left, right)


import math
l = [2,3,5,7,9,13]


low = int(input("low"))
high = int(input("high"))
left = l[0]
right = l[len(l)-1]


def binary_search(left, right):
  	if left>right:
    		return(False)
  	mid = floor((right-left)/2)+left
  	if l[mid] <high and l[mid] > low:
    		return (True)
  	elif l[mid] >high:
    		return(binary_search(left, mid-1))
  	elif l[mid] < low:
    		return(binary_search(mid+1, right))
  
x = binary_search(left,right)
print(x)
