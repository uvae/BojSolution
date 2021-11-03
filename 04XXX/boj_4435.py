for i in range(int(input())):
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	A = a[0]+a[1]*2+a[2]*3+a[3]*3+a[4]*4+a[5]*10
	B = b[0]+b[1]*2+b[2]*2+b[3]*2+b[4]*3+b[5]*5+b[6]*10
	print('Battle {}: {}'.format(i+1,
		'Evil eradicates all trace of Good' if B>A else 'Good triumphs over Evil' if A>B else 'No victor on this battle field'))