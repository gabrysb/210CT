n = int(input("_!"))  ##input
#starting point for the floating zeroes
flZero = 0
for i in range(1,20):
  #with every loop it increases the power of 5 by 1; until it hits a number that doesn't go into n, the mod is added to flZero
  if n//(5**i) > 0:
    flZero = flZero + n//(5**i)

print (flZero) ##output

#####################
#a. Does your algorithm have defined inputs and outputs?
	#Yes. Noted with comments by the code.
#b. Can you guarantee that it terminates?
	#Yes. There are no recursive functions and the for loop terminates after hitting i=20.
#c. Is it specified in a clear and concise manner?
	#Yes. The code is concise by using a for loop, and any variables are named appropriately.
#d. Does your algorithm produce the correct result for all instances?
	#Yes up until 2*(5**20). This can easily be modified by changing the latter number in the for loop.
#####################
