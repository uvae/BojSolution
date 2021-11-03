for _ in range(int(input())):
	d,n,s,p = map(int, input().split()); pt,st = d+n*p,n*s
	print('parallelize' if pt<st else 'do not parallelize' if pt>st else 'does not matter')