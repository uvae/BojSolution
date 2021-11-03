def gp(m):
	l = [True]*(m+1)
	for i in range(2,int(m**0.5)+1):
		if l[i]:
			for j in range(i*2,m+1,i): l[j] = False
	return [i for i in range(2,m+1) if l[i]]

m,n = map(int, input().split())
for i in gp(n):
	if(i>=m): print(i)