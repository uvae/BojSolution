from sys import stdin
input = stdin.readline

for _ in range(int(input())):
	n = list(map(int, input().split()))
	avg, t = float(sum(n[1::])/n[0]), 0
	for i in n[1::]:
		if(i > avg): t += 1

	print('{:0.3f}%'.format(round(t/n[0]*100, 3)))