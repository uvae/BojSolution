n,m = map(int, input().split())
dp,l = [[0]*(m+1) for _ in range(n+1)], [list(map(int,input().split())) for _ in range(n)]
for i in range(1,n+1):
	for j in range(1,m+1):
		dp[i][j] = l[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
for _ in range(int(input())):
	i,j,x,y = map(int, input().split())
	print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])