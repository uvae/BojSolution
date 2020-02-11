a,n = map(int, input().split())
b,m = map(int, input().split())
while(n>0 and m>0):
	n-=b;m-=a
print('DRAW' if n<1 and m<1 else 'PLAYER {}'.format('A' if n>m else 'B'))