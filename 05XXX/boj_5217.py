for _ in range(int(input())):
	l,n = [],int(input())
	for i in range(1,n):
		for j in range(i,n):
			if(i!=j and i<j and n==i+j): l.append('{} {}'.format(i,j))
	print('Pairs for {}: {}'.format(n, ', '.join(l)))