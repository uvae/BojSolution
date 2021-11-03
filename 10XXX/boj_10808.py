l = [0]*26
for i in input():
	l[ord(i)-97] += 1
print(' '.join(map(str,l)))