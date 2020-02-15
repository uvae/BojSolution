for i in range(int(input())):
	n,m = map(int, input().split())
	print('Scenario #{}:\n{}\n'.format(i+1,(m-n+1)*(n+m)//2))