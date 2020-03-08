import sys
def gcd(a, b):
	if(a == 0): return b
	return gcd(b % a, a)

n,l = sys.stdin.readline(),list(map(int, sys.stdin.readline().split()))
g = gcd(l[0], l[1] if len(l)==2 else gcd(l[1],l[2]))
for i in range(1, (g//2)+1):
	if not(g%i): print(i)
print(g)