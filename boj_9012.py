for _ in range(int(input())):
	s = []
	for i in input():
		if(i in '('): s.append(i)
		elif(i in ')'):
			if(s and s[-1]+i == '()'): del s[-1]
			else: s.append(i)
	print('NO' if s else 'YES')