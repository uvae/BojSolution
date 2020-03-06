while True:
	n,l = input().replace(' ',''), [0]*26
	if(n=='*'): break
	for i in n: l[ord(i)-97] = 1
	print('N' if l.count(0) else 'Y')