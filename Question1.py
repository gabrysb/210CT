""" Write a function that randomly shuffles an array of integers and explain the rationale behind its implementation. The reasoning behind this method is that I randomly pick out elements from a list and append them to a new list; I utilise the random.randint function as a means to generate a truly random integer that I then use as the position in the original list that I will copy the value from.
a. Does your algorithm have defined inputs and outputs?
	Yes. Noted in the code.
b. Can you guarantee that it terminates?
	Yes. There are no recursive functions and the for loop terminates after hitting i=20.
c. Is it specified in a clear and concise manner?
	Yes. The code is concise by using a for loop, and any variables are named appropriately.
d. Does your algorithm produce the correct result for all instances?
	Yes for all the lists I have tested."""

import random
length = int(input("How many numbers are you going to input?"))  ##input
list1 = []
count = 0
while count < length:
	#creates a list from user input
	x = int(input("Input number"))
list1.append(x)
 	count = count+1

taken = []
listRand = []

for i in range (0,length):
	listRand.append(i)

count1 = 0
while count1 < length:
 	y = random.randint(0,length-1)
 	#checks to see if the random number hasn't been use before
 	if y not in taken:
		#takes random integer and uses it to determine what position a value is taken from
   		taken.append(y)
   		listRand[count1] = list1[y]
   		count1 = count1+1
print(listRand) ##output
