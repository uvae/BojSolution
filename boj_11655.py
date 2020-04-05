for i in input():
	print(chr((ord(i)-65+13)%26+65 if 65<=ord(i)<=90 else (ord(i)-97+13)%26+97 if 97<=ord(i)<=122 else ord(i)), end='')