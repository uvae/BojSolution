n,f = int(input()),1
for i in range(1,10000):
	if(f>=n and f%2): print('{}/{}'.format(f-n%i+1 if n%i else 1,n%i if n%i else f)); break
	elif(f>=n and not(f%2)): print('{}/{}'.format(n%i if n%i else f,f-n%i+1 if n%i else 1)); break
	n-=f; f+=1