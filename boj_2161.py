l = [i for i in range(int(input()),0,-1)]
while l:
	print(l.pop(), end=' ')
	if(l): l.insert(0,l.pop())