n = int(input())
if not(n%2): print('I LOVE CBNU')
else:
	print('*'*n)
	for i in range(n//2+1):
		print('{}*{}'.format(' '*(n//2-i), ' '*(i*2-1)+'*' if i else ''))