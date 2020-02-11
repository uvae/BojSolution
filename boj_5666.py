while True:
	try:
		p,h = map(int, input().split())
		print('{:.2f}'.format(p/h))
	except EOFError:
		break