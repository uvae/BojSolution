import sys

a,b = 0,0
for _ in range(int(input())):
	A,B = map(int, sys.stdin.readline().split())
	a,b = a+(1 if A>B else 0), b+(1 if B>A else 0)
print(a,b)