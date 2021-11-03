while True:
	a,b = map(int, input().split())
	if (a,b)==(0,0): break
	print('{} {} / {}'.format(a//b, a%b, b))