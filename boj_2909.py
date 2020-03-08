def decimal(v,n):
	c,p = 10**(n-1),10**n
	return (v//p+1)*p if v//c%10 >=5 else v//p*p
c,k = map(int, input().split())
print(decimal(c,k))