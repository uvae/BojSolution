n, k = map(int, input().split())
l, r, o = [i for i in range(1, n+1)], [], 0
while l:
	o = (o + k - 1) % n; n -= 1
	r.append(l.pop(o))
print('<', end='')
print(*r, sep=', ', end='>')