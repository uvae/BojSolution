from itertools import combinations

def foker(l):
	m,d = [0]*4, [0]*13
	for i in l: m[i//13] += 1; d[i%13] += 1
	f = 1 if m.count(5) or m.count(6) else 0
	s = 1 if len(max(''.join(str(i) for i in d).split('0'), key=len)) >= 5 else 0
	s += 1 if d[0] and d[1] and d[2] and d[3] and d[4] else 2 if d[0] and d[12] and d[11] and d[10] and d[9] else 0

	if s==2 and f: return 11
	elif s and s!=3 and f: return 10
	elif d.count(4): return 9
	elif d.count(3) and d.count(2): return 8
	elif f: return 7
	elif s==3: return 6
	elif s==2: return 5
	elif s: return 4
	elif d.count(3): return 3
	elif d.count(2) >= 2: return 2
	elif d.count(2): return 1
	else: return 0

# with open('boj_1318_deck') as f:
# 	d = [tuple(line.strip().split()) for line in f.readlines()]
d = list(combinations([i for i in range(52)], 6))
l,s = [0]*12, len(d)

for i in d: l[foker(i)] += 1
print(l, sum(l), s)
for i in l: print('{}/{}'.format(i,s))