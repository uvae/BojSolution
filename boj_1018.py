## 문제 개요
# M * N 보드가 존재하며, 각 칸은 검은색 or 흰색으로 칠해져 있다. 이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다
# 체스판으로 만들기 위해 칸의 색을 다시 칠할 수 있다

# 8*8로 자른 후 칠을 가장 적게 할 수 있는 횟수

# 입력 : n(8~50) m(8~50), 체스판(WBW~)
# 출력 : N

# 처음 시작되는 패턴을 기반으로 8*8 칸으로 분석. 이후 최솟값은 p or 64-p 중 작은 값
# 반복 i(0, N-8) > j(0, M-8)
# 최솟값은 l[N-7][M-7] 리스트에 기록

def p(b, n, m):
	s, c = b[n][m], 0
	for i in range(n, n+8):
		for j in range(m, m+8):
			if(s != b[i][j]): c += 1
			s = 'W' if s == 'B' else 'B'
		s = 'W' if s == 'B' else 'B'
	return min(c, 64-c)

n, m = map(int, input().split())
b = [list(input()) for _ in range(n)]
l = [[64]*(m-7) for _ in range(n-7)]

for i in range(n-7):
	for j in range(m-7):
		l[i][j] = p(b, i, j)

print(min(map(min, l)))