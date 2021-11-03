# 소수
def gp(m):
	l = [True]*(m+1)
	for i in range(2,int(m**0.5)+1):
		if l[i]:
			for j in range(i*2,m+1,i): l[j] = False
	return [i for i in range(2,m+1) if l[i]]

n,k = map(int, input().split())
for i in gp(k):
	if(i!=k and n%i == 0): print('BAD', i); break
else: print('GOOD')