# 문제 개요 : N에 대한 분해합의 가장 작은 생성자 M
# 입력 : N(1 ~ 1,000,000)
# 출력 : N

# M을 구하기 위한 반복은 N - (N의 자릿수 * 9) ~ N

import sys

n = int(input())
l = len(str(n))

for i in range(n-l*9 if n-l*9 > 0 else 0, n):
	if(n == i + sum(int(i) for i in str(i))):
		print(i)
		sys.exit()
print(0)