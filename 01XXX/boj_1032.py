l = [input() for _ in range(int(input()))]; r=''
for c in range(len(l[0])):
	t = l[0][c]
	for i in range(len(l)-1):
		if(l[i+1][c] != t): r += '?'; break
	else: r += t
print(r)