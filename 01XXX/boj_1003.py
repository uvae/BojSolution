c0 = [1, 0] + [0]*39
c1 = [0, 1] + [0]*39

for i in range(2, 41, 1):
	c0[i] = c0[i-2] + c0[i-1]
	c1[i] = c1[i-2] + c1[i-1]

for t in range(int(input())):
	n = int(input())
	print(c0[n], c1[n])