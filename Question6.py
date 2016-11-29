INPUT string
strList <- DETERMINE string AS LIST
//each word is an element in the list
Reversed <- [ ]
FOR i = len(strList) to 0 where INCREMENT = -1


s = input("input your sentence")
strList = s.split()
reverse = []
for i in range(0,len(strList)):
  	reverse.append(0)
for x,y in zip(range(len(strList)-1, -1, -1), range(0, len(strList))):
  	reverse[x] = strList[y]
print(reverse)
