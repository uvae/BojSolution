def cc(l): return 1 if l[2] < l[1]+l[0] else 0
while True:
	a,b,c = map(int, input().split())
	if (a,b,c) == (0,0,0): break
	print('Invalid' if not cc(sorted([a,b,c])) else 'Equilateral' if a==b==c else 'Isosceles' if a==b or b==c or a==c else 'Scalene')