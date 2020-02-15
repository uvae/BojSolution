while True:
	m,t,v = input().split(); m,v=int(m),int(v)
	if (m,v,t)==(0,0,'W'): break
	m += v if t=='D' else v*-1
	print(m if m>=-200 else 'Not allowed')