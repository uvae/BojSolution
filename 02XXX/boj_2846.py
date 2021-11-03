input(); m,p,o = 0,0,0
for i in map(int, input().split()):
	o,p = o+i-p if i-p>0 and p else 0, i
	if(o>m): m=o
print(m)