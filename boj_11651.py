l = [list(map(int, input().split())) for _ in range(int(input()))]
for i in sorted(l, key=lambda e: (e[1], e[0])):
	print(i[0], i[1])