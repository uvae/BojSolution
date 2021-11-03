while True:
	a,b,c,d = map(int, input().split()); p = 0
	if (a,b,c,d)==(0,0,0,0): break
	while True:
		if(a==b==c==d): break
		a,b,c,d = abs(a-b),abs(b-c),abs(c-d),abs(d-a); p+=1
	print(p)