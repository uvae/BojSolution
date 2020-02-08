for _ in range(int(input())):
	a,b = 0,0
	for _ in range(int(input())):
		A,B = input().split()
		w = 0 if A==B else 1 if (A=='R' and B=='S') or (A=='S' and B=='P') or (A=='P' and B=='R') else 2
		(a,b) = (a+1,b) if w==1 else (a, b+1) if w==2 else (a,b)
	print('{} {}'.format('Player' if a!=b else 'TIE', 1 if a>b else 2 if b>a else ''))