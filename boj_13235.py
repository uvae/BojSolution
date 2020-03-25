s = input()
for i in range(len(s)//2):
	if(s[i] != s[len(s)-i-1]): print('false'); break
else: print('true')