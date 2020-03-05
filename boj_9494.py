while True:
	n,r = int(input()),0
	if not(n): break
	for _ in range(n):
		s = input()
		if(r > len(s)): continue
		for i in s[r:]:
			if(i==' '): break
			r += 1
	print(r+1)