import sys
n,c = map(int, input().split()); l=[0]*(c+1)
for _ in range(n):
	j = int(sys.stdin.readline())
	if(j == 1): l = [c]; break
	for i in range(j,c+1,j): l[i] = 1
print(sum(l))