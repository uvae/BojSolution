for _ in range(int(input())):
	a,b = input().split('-'); A,B = 0,0
	for i in range(len(a)):
		A += (ord(a[i])-65)*26**(len(a)-i-1)
	print('nice' if abs(int(b)-A)<=100 else 'not nice')