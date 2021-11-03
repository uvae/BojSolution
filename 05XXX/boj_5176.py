for _ in range(int(input())):
	p,m = map(int, input().split())
	l,s = [0]*(m+1),0
	for _ in range(p):
		a = int(input())
		if not(l[a]): l[a]=1
		else: s += 1
	print(s)