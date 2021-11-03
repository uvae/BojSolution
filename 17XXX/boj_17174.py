n,m = map(int, input().split()); c=n
while(n):
	n //= m; c += n
print(c)