l,n,r = [i**2 for i in range(1,501)],int(input()),0
for i in range(1,500):
	for j in range(0,i):
		if(l[i]-l[j]==n): r += 1
print(r)