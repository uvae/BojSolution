for i in input():
	print(chr(ord(i)-32) if i>='a' and i<='z' else chr(ord(i)+32), end='')