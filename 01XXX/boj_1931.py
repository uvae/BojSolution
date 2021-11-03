from sys import stdin
input = stdin.readline

a, m, cnt = [], 0, 0

for _ in range(int(input())):
	s, e = map(int, input().split())
	a.append((e, s))

a.sort()

for e, s in a:
	if s >= m:
		m = e
		cnt += 1

print(cnt)