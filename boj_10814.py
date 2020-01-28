## 문제 개요
# 회원들이 나이와 이름을 순서대로 주어준다. 이를 나이순, 가입순으로 정렬하여 출력하는 것이 목적이다
# 입력 : n(N : 1 ~ 200), n에 대한 <int> <string>
# 출력 : n에 대한 <int> <string>


l = [input().split() + [i] for i in range(int(input()))]
for i in sorted(l, key=lambda e: (int(e[0]), e[2])):
	print(i[0], i[1])