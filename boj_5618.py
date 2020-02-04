def gcd(a, b):
	while b: a, b = b, a%b
	return a

n,l = input(),list(map(int, input().split()))
g = gcd(l[0], l[1] if len(l)==2 else gcd(l[1],l[2]))
for i in range(1, g+1):
	if not(g%i): print(i)