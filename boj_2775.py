l = [[0]*15 for i in range(15)]
for i in range(0, 15):
	l[0][i] = i

for k in range(1, 15):
	for n in range(1, 15):
		l[k][n] = l[k-1][n] + l[k][n-1]

for _ in range(int(input())):
	k, n = int(input()), int(input())
	print(l[k][n])