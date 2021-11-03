n = list(map(int, input().split())); n[1] -= 45
if(n[1] < 0):
	n[0] = n[0]-1 if n[0]!=0 else 23
	n[1] += 60
print(n[0], n[1])