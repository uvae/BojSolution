l = {}

input()
for i in input().split():
	if not i in l: l[i] = 0
	l[i] += 1

input()
for i in input().split():
	print(l[i] if i in l else 0, end=' ')