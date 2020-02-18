n,m = map(int, input().split()); l={}
for _ in range(n+m):
	n = input()
	if not(n in l): l[n]=False
	else: l[n]=True
r = sorted([k for k,v in l.items() if v])
print('{}\n{}'.format(len(r), '\n'.join(r)))