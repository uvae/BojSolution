m,t = 0,0
for _ in range(int(input())):
	a, b, c = map(int, input().split())
	if(a == b == c): t = 10000 + a * 1000
	elif(a == b or b == c or a == c): t = 1000 + 100 * (a if a == b else c)
	else: t = max(a,b,c) * 100
	if(t > m): m = t
print(m)