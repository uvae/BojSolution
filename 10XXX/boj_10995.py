n = int(input())
for i in range(n):
	print('{}{}'.format(' ' if i%2 else '','* '*n))