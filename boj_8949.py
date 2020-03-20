a,b = map(list, input().split()); s=''
while a or b:
	x,y = a.pop() if a else '0', b.pop() if b else '0'
	s += str(int(x)+int(y))[::-1]
print(s[::-1])