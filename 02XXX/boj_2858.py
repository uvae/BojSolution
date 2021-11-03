r,b = map(int, input().split()); s = r+b
for i in range(3,int(s**0.5)+1):
	if((s//i-2)*(i-2)==b): print(s//i, i); break