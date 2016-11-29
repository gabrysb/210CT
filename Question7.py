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
