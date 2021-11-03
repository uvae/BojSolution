n, m = map(int, input().split())
j = [str(i) for i in range(1, n+1)]
m_len, cnt, res = n, 0, []

while j:
	cnt = (cnt+m-1) % m_len
	res.append(j.pop(cnt))
	m_len -= 1

print('<' + ', '.join(res) + '>')