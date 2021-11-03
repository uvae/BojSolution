def c9(n):
	T = "0123456789"
	q, r = divmod(n,9)
	if q==0: return T[r]
	else: return c9(q) + T[r]
print(c9(int(input())))