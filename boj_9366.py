def cc(l): return 1 if l[2] < l[1]+l[0] else 0
for i in range(int(input())):
	a,b,c = map(int, input().split())
	print('Case #{}: {}'.format(i+1, 'invalid!' if not cc(sorted([a,b,c])) else 'equilateral' if a==b==c else 'isosceles' if a==b or b==c or a==c else 'scalene'))