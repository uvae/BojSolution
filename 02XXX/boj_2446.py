n = int(input())
for i in range(n):
	print('{}{}'.format(' '*i, '*'*((n-i-1)*2+1)))
for i in range(n-1):
	print('{}{}'.format(' '*(n-i-2), '*'*((i+1)*2+1)))