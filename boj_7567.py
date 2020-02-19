s,p = 0,0
for i in input():
	s += 10 if i!=p else 5
	p = i
print(s)