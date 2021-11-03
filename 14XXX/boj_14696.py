from collections import Counter
for _ in range(int(input())):
	a,b = Counter(input().split()[1:]), Counter(input().split()[1:])
	for i in '4321':
		if(a[i] != b[i]): print('A' if a[i] > b[i] else 'B'); break
	else: print('D')