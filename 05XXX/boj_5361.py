l = [350.34, 230.9, 190.55, 125.3, 180.9]
for _ in range(int(input())):
	c = input().split()
	print('${:.2f}'.format(sum([int(c[i])*l[i] for i in range(5)])))