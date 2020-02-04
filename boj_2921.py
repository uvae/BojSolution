l = [0]
for i in range(1,int(input())+1):
	l.append(l[i-1]+int((i+1)*i*1.5))
print(l[-1])