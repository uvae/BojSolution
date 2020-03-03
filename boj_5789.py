for _ in range(int(input())):
	n = input(); l = len(n)
	print('Do-it' if n[l//2-1]==n[l//2] else 'Do-it-Not')