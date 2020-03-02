def gp(m):
	l = [True]*(m+1)
	for i in range(2,int(m**0.5)+1):
		if l[i]:
			for j in range(i*2,m+1,i): l[j] = False
	return l

p = gp(1040); n,s = input(),0
for i in n: s += ord(i)-96 if i>='a' and i<='z' else ord(i)-38
print('It is a prime word.' if p[s] else 'It is not a prime word.')