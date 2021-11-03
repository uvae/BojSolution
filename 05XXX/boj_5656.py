i=0
while True:
	c = input(); i+=1
	if('E' in c): break
	print('Case {}: {}'.format(i, str(eval(c)).lower()))