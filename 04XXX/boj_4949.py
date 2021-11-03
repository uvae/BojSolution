import sys

for l in sys.stdin:
	s, l = [], l.split('.')[0]
	if not l: break

	for i in l:
		if(i in '[('): s.append(i)
		elif(i in '])'):
			if(s and (s[-1]+i == '()' or s[-1]+i == '[]')): del s[-1]
			else: s.append(i)
	print('no' if s else 'yes')