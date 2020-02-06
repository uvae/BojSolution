for _ in range(int(input())):
	n,a = map(int, input().split())
	print('You get {} piece(s) and your dad gets {} piece(s).'.format(n//a, n%a))