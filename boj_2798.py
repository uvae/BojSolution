# 문제 개요 : 블랙잭

# 입력 : N(3 ~ 100) M(10 ~ 300,000)
# N에 대한 수
# 출력 : N

# 가능한 조합 출력 후 큰 조합순으로 반복하여, m에서 가장 가까운 수 출력

from itertools import permutations

n, m = map(int, input().split())
for i in sorted(list(map(sum, list(permutations(list(map(int, input().split())), 3)))), reverse=True):
	if(i <= m):
		print(i)
		break