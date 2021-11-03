for _ in range(int(input())):
	l = [0]*10
	for i in input(): l[ord(i)-48] = 1
	print(l.count(1))