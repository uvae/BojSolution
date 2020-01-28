from sys import stdin

n, m, k = map(int, stdin.readline().split())
l = [0] + [int(stdin.readline()) for _ in range(n)]

for _ in range(m+k):
	c, a, b = map(int, stdin.readline().split())
	if(c == 1): l[a] = b
	else: print(sum(l[a:b+1]))