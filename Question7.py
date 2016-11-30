"""
x <- 2
ISPRIME(n,x)
	IF n < x
		return False
	ELSE IF n = x
		return True
	ELSE IF n MOD x != 0
		CALL ISPRIME(n, x+1)
ELSE IF n MOD x = 0
		return False
	
IF prime = False
	OUTPUT “not a prime”
ELSE IF prime = True
	OUTPUT “is a prime”
Write a recursive function (pseudocode and code) to check if a number n is prime. In this the idea is to increase the input of the function until n (number to be tested) is divisible by x (variable starting at 2) or is equal to x. If n is divisible before x is equal to n, then the number isn’t prime. However if x is equal to n, then we’ve gone through all possible factors and the number is prime."""

n = int(input("enter number"))
x = 2
def is_prime(n,x):
if n < x:
   		return(False)
 	elif n == x:
   		return(True)
 	elif (n%x) != 0:
   		return(is_prime(n, x+1))
 	elif (n%x) == 0:
   		return(False)

y = is_prime(n,x)    
print(y)    
if y == False:
 	print("is not prime")
elif y == True:
 	print("is prime")
