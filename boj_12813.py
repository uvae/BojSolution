def bn(i,l):
	return ''.join(['1' if v=='0' else '0' for v in i])

A,B = input(), input(); sl = len(A) if A>B else len(B)
a,b = int(A,2),int(B,2)
print(bin(a&b)[2:].zfill(sl),
	bin(a|b)[2:].zfill(sl),
	bin(a^b)[2:].zfill(sl),
	bn(A,sl),
	bn(B,sl),
	sep='\n')