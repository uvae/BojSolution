c,s = 100,100
for _ in range(int(input())):
	a,b = map(int, input().split())
	c,s = (c,s-a) if a>b else (c-b,s) if b>a else (c,s)
print(c,s,sep='\n')