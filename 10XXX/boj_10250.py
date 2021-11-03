## 문제 개요
# 높이(H) x 방(W)의 호텔에 N번째 손님이 올 때 어느 방에 배치할 것인지에 대한 문제이다
# 손님은 엘레베이터에서 가까운 방을 선호하기에 101, 201호와 같이 층에 상관없이 가까운 방을 선호한다
# 이 때 N번째 손님에게 어느 방을 줘야할지 묻는 문제이다

# H,W : N(1 ~ 99)
# N : 1 ~ H*W
# T번의 테스트 케이스 동안 H W N을 입력받고
# 해당하는 호수를 출력 층 + 방번호

for _ in range(int(input())):
	h, w, n = map(int, input().split())
	if(n%h == 0): print('{0}{1:02d}'.format(h, n//h))
	else: print('{0}{1:02d}'.format(n%h, n//h+1))