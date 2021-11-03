n,m,r = map(int, input().split()); l,i,c = [0]*n,0,0
while l[i]+1!=m:
	l[i] += 1; c += 1
	i = (i+r)%n if l[i]%2 else (i-r)%n
print(c)