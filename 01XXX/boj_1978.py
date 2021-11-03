def cp(n):
	if(n == 2): return True
	if(n <= 1 or n%2 == 0): return False
	for i in range(3, n, 2):
		if(n%i == 0): return False
	return True

l = [i for i in range(1, 1001) if cp(i)]
n, c = input(), 0

for i in map(int, input().split()):
	if(i in l): c += 1
print(c)