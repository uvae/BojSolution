s = 0
n,t = map(int, input().split())
for i in map(int, input().split()):
	t-=i; s += 1 if t>=0 else 0
print(s)