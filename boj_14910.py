p,r=-1000001,True
for i in map(int, input().split()):
	if(i<p): r=False; break
	p=i
print('Good' if r else 'Bad')