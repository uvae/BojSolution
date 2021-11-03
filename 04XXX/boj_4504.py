n = int(input())
while True:
	a = int(input())
	if not(a): break
	print('{} is {}a multiple of {}.'.format(a,'NOT ' if a%n else '',n))