for _ in range(int(input())):
	l = sorted(map(int, input().split()))
	print('KIN' if l[3]-l[1]>=4 else sum(l[1:4]))