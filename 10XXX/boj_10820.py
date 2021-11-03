import sys
while True:
	n = sys.stdin.readline()
	if not(n): break
	s,d,c,b = 0,0,0,0
	for i in n:
		i = ord(i)
		if(i==32): b+=1
		elif(i>=48 and i<=57): c+=1
		elif(i>=65 and i<=90): d+=1
		elif(i>=97 and i<=122): s+=1
	print(s,d,c,b)