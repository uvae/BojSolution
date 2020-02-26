a,b = input().split()
al,bl,s = [0]*10,[0]*10,0
for i in a: al[ord(i)-48]+=1
for i in b: bl[ord(i)-48]+=1
for i in range(1,10):
	for j in range(1,10):
		s += i*j*(al[i]*bl[j])
print(s)