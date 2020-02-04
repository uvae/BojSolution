l = [list(map(int, input().split())) for _ in range(9)]
m,i,j = 0,0,0
for r in range(9):
	for c in range(9):
		if(l[r][c] > m): m,i,j = l[r][c],r+1,c+1
print('{}\n{} {}'.format(m,i,j))