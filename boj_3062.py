for _ in range(int(input())):
	n = input(); s = str(int(n) + int(n[::-1]))
	for i in range(0,len(s)//2):
		if(s[i]!=s[len(s)-i-1]): print('NO'); break
	else: print('YES')