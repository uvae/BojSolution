'''
1 0 0 0 0
1 1 0 0 0
1 2 1 0 0
1 3 3 1 0
1 4 6 4 1
1 5 10 10 5 1
'''

n, k = map(int, input().split())
l = [[1] + [0]*k for _ in range(n+1)]

for i in range(1, n+1):
	for j in range(1, k+1):
		l[i][j] = l[i-1][j-1] + l[i-1][j]

print(l[n][k])