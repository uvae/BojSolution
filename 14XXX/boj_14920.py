n,i = int(input()),1
while n!=1:
	n,i = 3*n+1 if n%2 else n//2, i+1
print(i)