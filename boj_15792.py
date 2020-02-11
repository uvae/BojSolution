a,b=map(int,input().split())
r,n=str(a//b)+'.',a%b
for i in range(1000):
	n *= 10; m = n//b
	r += str(m);n %= b
	if not(n): break
print(r)