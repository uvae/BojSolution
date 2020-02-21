s,M = 0,0
for _ in range(10):
	m,p = map(int, input().split())
	s += p-m
	if(s>M): M=s
print(M)