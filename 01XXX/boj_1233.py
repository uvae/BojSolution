a,b,c = map(int, input().split()); l = [0]*81
for i in range(1,a+1):
	for j in range(1,b+1):
		for k in range(1,c+1): l[i+j+k]+=1
print(l.index(max(l)))