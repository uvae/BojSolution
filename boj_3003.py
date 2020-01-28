l = [1, 1, 2, 2, 2, 8]
for i in map(int, input().split()):
	print(l.pop(0) - i, end=' ')