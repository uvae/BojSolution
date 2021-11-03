l,t,s = [input() for _ in range(8)],True,0
for i in range(8):
	for j in range(8):
		if(l[i][j]=='F' and t): s+=1
		t=not(t)
	t=not(t)
print(s)