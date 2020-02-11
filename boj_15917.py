from sys import stdin
l = [2**i for i in range(0,32)]
for _ in range(int(stdin.readline())):
	print(1 if int(stdin.readline()) in l else 0)