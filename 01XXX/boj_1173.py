N,m,M,T,R = map(int, input().split()); x,c=m,0
while N:
	c += 1
	if(x+T <= M): x+=T; N-=1; continue
	x = x-R if x-R>=m else m
	if(x==m and x+T>M): c=-1; break
print(c)