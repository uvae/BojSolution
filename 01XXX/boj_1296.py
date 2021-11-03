nm,m,n = input(),-1,''
for i in sorted([input() for _ in range(int(input()))]):
	l,o,v,e = nm.count('L')+i.count('L'),nm.count('O')+i.count('O'),nm.count('V')+i.count('V'),nm.count('E')+i.count('E')
	s = ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))%100
	if(s>m): m,n = s,i
print(n)