for _ in range(int(input())):
	s = 0
	for _ in range(int(input())):
		a,b,c = map(int, input().split())
		s += max(a,b,c) if max(a,b,c)>0 else 0
	print(s)