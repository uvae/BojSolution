l = [0,1] + [0]*99
for i in range(2,101):
	l[i] = l[i-1] + i**2

while True:
	n = int(input())
	if not(n): break
	print(l[n])