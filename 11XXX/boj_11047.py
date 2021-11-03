n,k = map(int, input().split()); c=0
for m in reversed([int(input()) for _ in range(n)]):
	k,c = k-k//m*m, c+k//m
print(c)