while True:
	s,p = input(),''
	if s=='0': break
	for i in s.split()[1:]:
		if(i==p): continue
		print(i, end=' '); p=i
	print('$')