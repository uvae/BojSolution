for _ in range(int(input())):
	n,m = map(int, input().split())
	print(-1 if m<4 or n<12 else 11*m+4)