for _ in range(int(input())):
	a,b = map(int, input().split()); s = input()
	for i in s: print(chr((a*(ord(i)-65)+b)%26+65), end='')
	print()