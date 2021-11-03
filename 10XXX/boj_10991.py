n = int(input())
for i in range(n):
	if(i+1 != n): print('{}{}'.format(' '*(n-i-1), '*'+' '*((i-1)*2+1)+('*' if i else '')))
	else: print('{}'.format('*'*(i*2+1)))