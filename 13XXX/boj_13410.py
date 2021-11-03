n,k = map(int,input().split()); m=0
for i in range(1,k+1):
	v = int(str(n*i)[::-1])
	if(v>m): m=v
print(m)