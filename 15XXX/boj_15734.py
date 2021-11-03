l,r,a = map(int, input().split())
while a:
	if(l<r): l+=1
	else: r+=1
	a-=1
print(l+r-abs(l-r))