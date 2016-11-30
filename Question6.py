"""
INPUT string
strList <- DETERMINE string AS LIST
//each word is an element in the list
reversed <- []
FOR i = 0 to len(strList)
	APPEND 0 TO REVERSED
FOR x = len(strList) to 0 where INCREMENT = -1 and y = 0 to len(strList)
	reversed[x] <- strList[y]
OUTPUT reversed
Write the pseudocode and code for a function that reverses the words in a sentence. Input: "This is awesome" Output: "awesome is This". Give the Big O notation. The code generates a list from a string input and then generates a list of the same size. You then iterate through both lists, one from the start and one from the end until you fill up the reversed list.
The Big O notation for this is O(n)."""

s = input("input your sentence")
strList = s.split()
reverse = []
for i in range(0,len(strList)):    #O(n)
 	reverse.append(0)
for x,y in zip(range(len(strList)-1, -1, -1), range(0, len(strList))): ##O(n)
 	reverse[x] = strList[y]
print(reverse)
