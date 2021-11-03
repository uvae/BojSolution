import sys

l = [0]*26
while True:
	n = sys.stdin.readline()
	if not(n): break
	for c in n:
		if(ord(c)!=10 and ord(c)!=32): l[ord(c)-97] += 1
for i in range(0,26):
	print(chr(i+97) if l[i]==max(l) else '', end='')