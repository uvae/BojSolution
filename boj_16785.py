a,b,c = map(int, input().split())
for i in range(1, c+1):
	if(c <= a*i + i//7*b): print(i); break