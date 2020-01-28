l = [list(map(int, input().split())) for _ in range(int(input()))]
for i in sorted(l, key=lambda e: (e[0], e[1])):
	print(i[0], i[1])