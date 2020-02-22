from itertools import combinations
l = list(combinations([int(input()) for _ in range(9)], 7))
for i in l:
	if(sum(i)==100): print('\n'.join(map(str,i)))