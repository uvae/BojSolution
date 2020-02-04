n = int(input())
for i in range(n):
	print('{}{}'.format(' '*(n-i-1), '*'*(i+1)))
for i in range(n-1):
	print('{}{}'.format(' '*(i+1), '*'*(n-i-1)))