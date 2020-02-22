l,s = [[0]*101 for _ in range(101)],0
for _ in range(4):
	x1,y1,x2,y2 = map(int, input().split())
	for i in range(y1,y2):
		for j in range(x1,x2):
			l[i][j],s = 1,s+1 if not(l[i][j]) else s
print(s)