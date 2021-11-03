l = [0,1,0,0]
for _ in range(int(input())):
	a,b = map(int, input().split())
	l[a], l[b] = l[b], l[a]
print(l.index(1))