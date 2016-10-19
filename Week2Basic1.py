maxRng = int(input("Set highest parameter"))
temp = 0
for i in range (1,maxRng+1):
  x = i**0.5
  if x%1 ==0 and i>temp:
    temp = i
print(temp)
