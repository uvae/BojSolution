n = int(input())
for i in range(n):
	print('{1}{0}{1}'.format(' '*((n-i-1)*2), '*'*(i+1)))
for i in range(n-1):
	print('{1}{0}{1}'.format(' '*((i+1)*2), '*'*(n-i-1)))