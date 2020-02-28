input(); l = map(int, input().split())
c,s = int(input()),0
for i in l:
	s += i//c*c + (c if i%c else 0)
print(s)