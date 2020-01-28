from sys import stdin
from collections import deque
input = stdin.readline

def bfs():
	c = [[False]*m for i in range(n)]
	q = deque()
	c[0][0] = True
	q.append((0, 0))

	while q:
		x, y = q.popleft()
		for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
			nx, ny = x+dx, y+dy
			if nx<0 or nx>=n or ny<0 or ny>=m: continue
			if not c[nx][ny]:
				if a[nx][ny] >= 1: a[nx][ny] += 1
				else:
					q.append((nx, ny))
					c[nx][ny] = True

def melt():
	check = False

	for r in range(n):
		for c in range(m):
			if(a[r][c] >= 3):
				a[r][c] = 0
				check = True

			elif(a[r][c] == 2):
				a[r][c] = 1
				check = True

	return check

n, m = map(int, input().split())
a, cnt = [[0]*m for i in range(n)], 0
a = [list(map(int, input().split())) for _ in range(n)]

while True:
	bfs()
	if not melt(): break
	else: cnt += 1

print(cnt)