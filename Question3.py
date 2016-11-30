"""
INPUT maxRng
FOR i = 1 to maxRng
	X <- i ^ 0.5
	IF x % 1 = 0 AND i > temp
		temp <- i
	END IF
END FOR
OUTPUT temp

Write the pseudocode for a function which returns the highest perfect square which is less or equal to its parameter (a positive integer). Implement this in the programming language of your choice. This simply goes through a set of numbers up to the maximum and when it finds a perfect square, sets it as temp."""

maxRng = int(input("Set highest parameter"))
temp = 0
for i in range (1,maxRng+1):
 	x = i**0.5
 	if x%1 ==0 and i>temp:
   		temp = i
print(temp)
