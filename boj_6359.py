for _ in range(int(input())):
	n = int(input())
	l = [False]*n
	for i in range(1,n+1):
		for t in range(i-1,n,i):
			l[t] = not(l[t])
	print(l.count(True))