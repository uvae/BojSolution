n,p = map(int, input().split())
l,a = [0]*98,n
while True:
	a = a*n%p; l[a]+=1
	if(l[a]>2): break
print(l.count(2)+1)