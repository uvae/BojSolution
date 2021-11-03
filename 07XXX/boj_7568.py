# 문제 개요 : (kg, cm)을 기준으로 덩치의 순위를 매긴다
# A(kg) > B(kg) && A(cm) > B(cm) 조건을 만족해야 덩치가 더 크다고 볼 수 있다

# 입력 : 사람 수 n, n애 대한 KG CM
# 출력 : 입력받은 순서대로의 순위(N N N ...)

l = [list(map(int, input().split())) for i in range(int(input()))]

for i in range(len(l)):
	r = 1
	for j in range(len(l)):
		if(l[i][0] < l[j][0] and l[i][1] < l[j][1]): r += 1
	print(r, end=' ')
