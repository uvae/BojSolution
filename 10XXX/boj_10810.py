n,m = map(int, input().split()); l = [0]*n
for _ in range(m):
	i,j,k = map(int, input().split())
	for v in range(i-1,j):
		l[v] = k
print(*l)