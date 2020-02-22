a,b = list(map(int, input().split())), list(map(int, input().split()))
A,B = 0,0
for i in range(10):
	A,B = A+1 if a[i]>b[i] else A, B+1 if b[i]>a[i] else B
print('A' if A>B else 'B' if B>A else 'D')