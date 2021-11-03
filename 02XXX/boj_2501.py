l = []
n, k = map(int, input().split())
for i in range(1,n+1):
	if not(n%i): l.append(i)
print(0 if k>len(l) else l[k-1])