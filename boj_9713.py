l = [0,1,1] + [0]*98
for i in range(3,101):
	l[i] = (i if i%2 else i-1) + l[i-2]
for _ in range(int(input())):
	print(l[int(input())])