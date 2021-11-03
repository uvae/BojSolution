n,a,b = input(),0,0
for i in map(int, input().split()):
	a,b = a+(i//30+1)*10, b+(i//60+1)*15
print('Y' if a<b else 'M' if a>b else 'Y M', a if a<b else b)