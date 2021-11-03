n = int(input())
for i in range(n, 0, -1):
	print('{}{}'.format(' '*(n-i), '*'*(i*2-1)))