s,t = int(input()),0
while True:
	c = input()
	if(c=='='): break
	elif(c.isdigit()): s = eval(str(s)+t+c)
	else: t = c if c!='/' else '//'
print(s)