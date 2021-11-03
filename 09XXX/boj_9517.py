n,t = int(input())-1, 210
for _ in range(int(input())):
	a,r = input().split()
	t -= int(a)
	n += 1 if r=='T' and t>0 else 0
print(n if n<=8 else n%8)