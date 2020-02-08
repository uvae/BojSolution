dp, n = [0]*1000001, int(input())
for i in range(2, n+1, 1):
    m = dp[i-1]+1
    if(i%3 == 0):
        if(m>dp[int(i/3)]+1): m = dp[int(i/3)]+1
    if(i%2 == 0):
        if(m>dp[int(i/2)]+1): m = dp[int(i/2)]+1
    dp[i] = m
print(dp[n])
