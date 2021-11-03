for _ in range(int(input())):
	n = int(input())
	for i in range(n):
		print('#{}{}'.format(('#' if i==0 or i==n-1 else 'J')*(n-2), '#' if n!=1 else ''))
	print('')