from sys import stdin
input = stdin.readline

n, cnt = int(input()), 0
bList = list(map(int, input().split()))

for i in range(n-1):
	for j in range(n-1-i):
		if(bList[j] > bList[j+1]):
			bList[j], bList[j+1] = bList[j+1], bList[j]
			cnt += 1

print(cnt)