l,u = [1], [0]*1001
for i in range(2,50):
	l.append(l[-1]+i)
for i in l:
	for j in l:
		for k in l:
			if(i+j+k<=1000): u[i+j+k]=1
for _ in range(int(input())):
	print(u[int(input())])