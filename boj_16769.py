l = [list(map(int,input().split())) for _ in range(3)]
for i in range(100):
	p,n = i%3, (i+1)%3
	over = l[p][1]+l[n][1]-l[n][0] if l[n][0] < l[p][1]+l[n][1] else 0
	l[n][1] += l[p][1] - over
	l[p][1] = over
for i in l:
	print(i[1])