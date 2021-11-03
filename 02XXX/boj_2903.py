l = [2]
for i in range(1,int(input())+1):
	l.append(l[i-1]*2-1)
print(l[-1]**2)