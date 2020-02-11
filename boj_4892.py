i=0
while True:
	n,i = int(input())*3,i+1
	if(n==0): break
	print('{}. {} {}'.format(i, 'odd' if n%2 else 'even',(n+1)//6 if n%2 else n//6))