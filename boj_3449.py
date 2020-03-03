for _ in range(int(input())):
	a,b = input(),input(); l,s = len(a),0
	for i in range(l):
		if(a[i]!=b[i]): s += 1
	print('Hamming distance is {}.'.format(s))