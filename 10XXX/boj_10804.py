l = [i for i in range(1,21)]
for _ in range(10):
	a,b = map(int, input().split()); a-=1; b-=1
	l[a:b+1] = reversed(l[a:b+1])
print(*l)