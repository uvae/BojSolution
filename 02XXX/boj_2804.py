a,b = input().split()
la,lb,sa,sb = len(a),len(b),0,0
for i in a:
	if(i in b): sa,sb=a.index(i),b.index(i); break
for i in range(lb):
	print('{}'.format(a if i==sb else '.'*sa + b[i] + '.'*(la-sa-1)))