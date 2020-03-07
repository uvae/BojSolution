from collections import Counter

m = 0
for _ in range(int(input())):
	l,s = Counter(map(int, input().split())),0
	c = list(l.values()).count(2)
	for key,val in l.items():
		if(val==4): s += 50000+key*5000
		elif(val==3): s += 10000+key*1000
		elif(val==2): s += key*(500 if c==2 else 100)
	s += 2000 if c==2 else 1000 if c==1 else max(l.keys())*100 if len(l)==4 else 0
	m = max(m,s)
print(m)