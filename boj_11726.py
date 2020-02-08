dp,n = [1, 1] + [0]*999, int(input())
for i in range(2, n+1, 1): dp[i] = dp[i-1]+dp[i-2]
print(dp[n]%10007)
print(dp)
