n,m = map(int, input().split())
l = [0]*1001; s = 0
for i in map(int, input().split()):
	for v in range(i,n+1,i):
		if(l[v]): continue
		s+=v; l[v]=1
print(s)