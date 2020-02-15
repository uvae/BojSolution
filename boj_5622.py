l,s = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'],0
for i in input():
	for t in range(len(l)):
		if(i in l[t]): s += t+3; break
print(s)