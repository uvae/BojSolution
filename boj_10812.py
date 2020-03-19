n,m = map(int, input().split())
l = [i+1 for i in range(n)]
for _ in range(m):
	i,j,k = map(int, input().split())
	l[i-1:j] = l[k-1:j] + l[i-1:k-1]
print(*l)