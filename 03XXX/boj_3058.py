for _ in range(int(input())):
	l = list(filter(lambda e: e%2==0, map(int, input().split())))
	print(sum(l), min(l))