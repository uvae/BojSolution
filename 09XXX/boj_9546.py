l = [0,1]+[0]*29
for i in range(2,31):
	l[i] = 2*l[i-1]+1
for _ in range(int(input())):
	print(l[int(input())])