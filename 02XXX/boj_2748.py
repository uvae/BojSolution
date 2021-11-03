n, l = int(input()), [0, 1] + [0]*89
for i in range(2, n+1):
	l[i] = l[i-1] + l[i-2]
print(l[n])