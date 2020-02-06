n,s,i = input(),0,1
for n in map(int, input().split()):
	print(n*i-s, end=' ')
	s+=n if s==0 else n*i-s;i+=1