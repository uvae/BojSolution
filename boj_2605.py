n,l = int(input()), []
s = list(map(int,input().split()))
for i in range(n):
	l.insert(s[i],str(i+1))
print(' '.join(reversed(l)))