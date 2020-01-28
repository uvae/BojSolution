# N개의 단어를 받아 정렬하는 것이 목적
# 정렬의 우선순위는 1. 길이가 짧은 것 2. 길이가 같으면 사전 순으로
# 중복은 제거한다

# N : 1 ~ 20,000
# String : 1 ~ 50

for s in sorted(set([input() for _ in range(int(input()))]), key=lambda e: (len(e), e)):
	print(s)