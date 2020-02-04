for _ in range(3):
	l = list(map(int, input().split()))
	h,m,s = l[3]-l[0], l[4]-l[1], l[5]-l[2]
	m += (-1 if s<0 else 1 if s>59 else 0); s %= 60
	h += (-1 if m<0 else 1 if m>59 else 0); m %= 60
	print(h,m,s)