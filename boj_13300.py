n,k = map(int, input().split())
l,r = [[0,0] for _ in range(6)],0
for _ in range(n):
	s,y = map(int, input().split())
	l[y-1][s] += 1
for i in l:
	r += i[0]//k + (1 if i[0]%k else 0) + i[1]//k + (1 if i[1]%k else 0)
print(r)