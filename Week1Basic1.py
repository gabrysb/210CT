import random
length = int(input("How many numbers are you going to input?"))  ##input
list1 = []
count = 0
#creates original array
while count < length:
  x = int(input("Input number"))
  list1.append(x)
  count = count+1

taken = []
listRand = []

#creates array ready to have values inserted
for i in range (0,length):
  listRand.append(i)

#takes random values from original list and places them in the new list
count1 = 0
while count1 < length:
  y = random.randint(0,length-1)
  #checks to see if the random number hasn't been use before
  if y not in taken:
    taken.append(y)
    listRand[count1] = list1[y]
    count1 = count1+1
print(listRand) ##output

#####################
#a. Does your algorithm have defined inputs and outputs?
	#Yes. Noted with comments by the code.
#b. Can you guarantee that it terminates?
	#Yes. There are no recursive functions and the for loop terminates after hitting i=20.
#c. Is it specified in a clear and concise manner?
	#Yes. The code is concise by using a for loop, and any variables are named appropriately.
#d. Does your algorithm produce the correct result for all instances?
	#Yes for all the lists I have tested.
#####################
