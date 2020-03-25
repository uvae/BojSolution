input(); l = list(map(int, input().split())); L,M = len(l),0
for i in range(L):
	if(i>=1 and M >= len(l[i+1:])): break
	m = 0
	for j in range(i+1,L):
		if(l[i]>l[j]): m+=1
		else: break
	M = m if m>M else M
print(M)