for _ in range(int(input())):
	c,r = input().split('=')
	print('correct' if eval(c)==int(r) else 'wrong answer')