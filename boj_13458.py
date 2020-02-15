import math
s = int(input())
l=map(int, input().split())
b,c = map(int, input().split())
for i in l:
	s += math.ceil((i-b)/c) if i-b>0 else 0
print(s)