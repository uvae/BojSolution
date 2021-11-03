i=0
while True:
	l = list(map(int, input().split())); i+=1
	if l==[0]: break
	print('Pizza {} {} on the table.'.format(i, 'fits' if (2*l[0])**2 >= l[1]**2+l[2]**2 else 'does not fit'))