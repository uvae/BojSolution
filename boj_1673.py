import sys
while True:
	i = sys.stdin.readline()
	if not(i): break
	n,k = map(int, i.split()); s=n
	while n//k:
		s,n = s+n//k, n//k+n%k
	print(s)