n,f = int(input()),1
for i in range(1,100):
	if(f>=n): print(f-n%i+1 if n%i else 1,n%i if n%i else f); break
	n-=f; f+=1