n,k,c = int(input()),1,0
while n>0:
	(n,k) = (n-k,k+1) if n-k>=0 else (n-1,2); c += 1
print(c)