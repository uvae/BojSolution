while True:
	a,b,c = map(int, input().split())
	if (a,b,c) == (0,0,0): break
	t = 'AP' if b-a == c-b else 'GP'
	print(t, c+c-b if t=='AP' else c*(c//b))