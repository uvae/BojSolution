import sys
from collections import Counter

n = int(sys.stdin.readline())
l = sorted([int(sys.stdin.readline()) for _ in range(n)])
l_c = Counter(l).most_common()

print(
	round(sum(l)/n),
	l[n//2],
	l_c[0][0] if n == 1 or l_c[0][1] != l_c[1][1] else l_c[1][0],
	l[-1] - l[0], sep='\n'
)