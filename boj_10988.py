s = input(); l = len(s)
for i in range(l//2):
	if(s[i] != s[l-i-1]): print(0); break
else: print(1)