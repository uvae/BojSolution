for _ in range(int(input())):
	a,b = map(int, input().split());a*=a;b*=b
	print(a//b+(1 if a%b else 0))