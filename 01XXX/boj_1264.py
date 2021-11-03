while True:
	n,s = input(),0
	if(n=='#'): break
	for i in 'aeiouAEIOU': s += n.count(i)
	print(s)