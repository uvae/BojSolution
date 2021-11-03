n, res = int(input()), 0

for i in range(1, n+1):
	if(i < 100): res += 1
	else:
		t = str(i)
		if(int(t[2])-int(t[1]) == int(t[1])-int(t[0]) ): res += 1

print(res)