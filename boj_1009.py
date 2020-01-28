### 문제 풀이 띵킹..

# 문제에서 요구하는 것 : 입력받은 값으로 제곱연산을 수행하였을 때 마지막 1의 자리
# 알고리즘으로 해야하는 것 : 제곱의 규칙성에 따라 마지막 자리의 숫자

'''
t = int(input())
a, b = map(int, input().split())
c = a ^ b

1 ^ N = 1
2 ^ N = 2, 4, 8, 6 ...
3 ^ N = 3, 9, 7, 1 ...
4 ^ N = 4, 6 ...
5 ^ N = 5
6 ^ N = 6
7 ^ N = 7, 9, 3, 1 ...
8 ^ N = 8, 4, 2, 6 ...
9 ^ N = 9, 1 ...
10 ^ N = 0
11 ^ N = 1
12 ^ N = 2, 4, 8, 6 ...
13 ^ N = 3, 9, 7, 1
'''

# 규칙성 : 문제에서 원하는 1의 자리는 0~9까지만 알게되면 이후는 반복적인 곱셈에 지나지 않는다
# 또한, 소수가 아닌 다른수의 곱으로 나타나는 수의 경우에는 이전 규칙에서 크게 벗어나지 못한다
# 10 미만의 합성 수에서 같은 숫자로만 이루어지면, 그 숫자의 개수에 따라 건너뛰는 카운트가 정해진다 2*2 = 2씩, 2*2*2 = 3씩
# 6과 같은 다른수의 합성의 경우 각 반복되는 숫자의 곱으로 확인이 가능하다

## 문제풀이 알고리즘

l = [[10], [1], [2,4,8,6], [3,9,7,1], [4,6], [5], [6], [7,9,3,1], [8,4,2,6], [9,1]]

for _ in range(int(input())):
	a, b = map(int, input().split())
	a %= 10

	print(l[a][(b-1) % len(l[a])])