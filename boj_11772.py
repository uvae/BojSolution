s = 0
for _ in range(int(input())):
	n = input(); s += int(n[:-1])**int(n[-1])
print(s)