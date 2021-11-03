r,d = 1,0
for _ in range(int(input())):
	a,b,s = map(int, input().split())
	r,d = r//a*b,(d+s)%2
print(d,r)