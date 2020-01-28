# from collections import deque

# def dfsSearch(n, c):
# 	c[n] = True
# 	print(n, end=' ')
# 	for i in range(1, node+1):
# 		if a[n][i] == 1 and c[i] is False:
# 			dfsSearch(i, c)

# 	return n

# def dfs(start):
# 	c = [False] * (node+1)
# 	res = dfsSearch(start, c)
# 	return res

# def bfs(start):
# 	visit = []
# 	c = [False] * (node+1)
# 	q = deque()
# 	q.append(start)
# 	c[start] = True

# 	while q:
# 		n = q.popleft()
# 		if n not in visit:
# 			visit.append(n)
# 			for i in range(1, node+1):
# 				if a[n][i] == 1 and c[i] is False:
# 					c[i] = True
# 					q.append(i)

# 	return visit

# node, link, v = map(int, input().split())
# a = [ [0 for _ in range(node+1)] for _ in range(node+1) ]

# for _ in range(link):
# 	tn, tl = map(int, input().split())
# 	a[tn][tl] = 1
# 	a[tl][tn] = 1

# print(bfs(v))
# print(dfs(v))

from collections import deque

def dfs(n):
	c[n] = True
	print(n, end=' ')

	for i in range(1, node+1):
		if a[n][i] and not(c[i]): dfs(i)

def bfs(s):
	c = [False] * (node+1)
	q = deque()
	q.append(s)
	c[s] = True

	while q:
		n = q.popleft()
		print(n, end=' ')

		for i in range(1, node+1):
			if a[n][i] and not(c[i]):
				c[i] = True
				q.append(i)

node, link, v = map(int, input().split())
a = [ [0 for _ in range(node+1)] for _ in range(node+1) ]

for _ in range(link):
	n, l = map(int, input().split())
	a[n][l] = 1
	a[l][n] = 1

c = [False] * (node+1)

dfs(v)
print()
bfs(v)