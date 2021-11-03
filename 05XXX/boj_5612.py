n,m,M = int(input()),int(input()),0
for _ in range(n):
	a,b = map(int, input().split())
	m = m+a-b
	if(m>M): M=m
	elif(m<0): M=0; break
print(M)