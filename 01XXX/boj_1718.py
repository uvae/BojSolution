n,k,r = input(),input(),''
nl,kl = len(n),len(k)
for i in range(nl):
	if(n[i] == ' '): r += ' '; continue
	c = ord(n[i])-ord(k[i%kl])
	r += chr(c + (26 if c<=0 else 0)+96)
print(r)