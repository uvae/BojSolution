# 장부에 돈을 기입하고 총 금액을 출력한다
# 그러나 0이 입력되면, 바로 전에 작성한 숫자는 잘못된 숫자라 지워야 한다

l = []
for _ in range(int(input())):
	i = int(input())
	if(i == 0 and l): l.pop()
	else: l.append(i)
print(sum(l))