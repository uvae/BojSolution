for i in range(int(input())):
	l = sorted(map(int, input().split()))
	print('Scenario #{}:\n{}\n'.format(i+1, 'yes' if l[2]**2==l[1]**2+l[0]**2 else 'no'))