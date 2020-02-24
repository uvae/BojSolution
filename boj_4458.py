for _ in range(int(input())):
	s = input()
	print(s[0] if s[0]>='A' and s[0]<='Z' else chr(ord(s[0])-32), s[1:], sep='')