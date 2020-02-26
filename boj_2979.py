a,b,c = map(int, input().split())
l,s = [0]*101, 0
for _ in range(3):
	x,y = map(int, input().split())
	for i in range(x,y): l[i]+=1
for i in l:
	s += (a if i==1 else b if i==2 else c if i==3 else 0)*i
print(s)