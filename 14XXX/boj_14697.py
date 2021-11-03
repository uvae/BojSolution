a,b,c,n = map(int, input().split())
l = [0]*301; l[a]=1; l[b]=1; l[c]=1
for i in range(1,n+1):
	l[i] = 1 if l[i] or l[i-a] or l[i-b] or l[i-c] else 0
print(l[n])