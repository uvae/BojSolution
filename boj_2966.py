l,n = int(input()),input()
a,b,c = 0,0,0
for i in range(l):
	if(n[i] == ['A','B','C'][i%3]): a+=1
	if(n[i] == ['B','A','B','C'][i%4]): b+=1
	if(n[i] == ['C','C','A','A','B','B'][i%6]): c+=1
M = max(a,b,c); print(M)
if(a==M): print('Adrian')
if(b==M): print('Bruno')
if(c==M): print('Goran')