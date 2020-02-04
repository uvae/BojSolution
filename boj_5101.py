while True:
	a,b,c = map(int, input().split())
	if (a,b,c) == (0,0,0): break
	print('X' if (c-a)%b else (c-a)//b+1)