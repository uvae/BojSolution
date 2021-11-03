for _ in range(int(input())):
	s,g = 0, 0
	for _ in range(int(input())):
		a,b = map(float, input().split())
		s+=a;g+=a*b
	print(int(s),round(g/s,1))
