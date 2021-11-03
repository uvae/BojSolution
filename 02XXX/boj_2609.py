def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

a, b = map(int, input().split())
print(gcd(a, b), int(a*b/gcd(a, b)), sep='\n')