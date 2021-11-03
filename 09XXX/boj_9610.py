l,a = [0]*4,0
for _ in range(int(input())):
	x,y = map(int, input().split())
	if(x == 0 or y == 0): a += 1
	else: l[0 if x>0 and y>0 else 1 if x<0 and y>0 else 2 if x<0 and y<0 else 3] += 1
for i in range(4): print('Q{}: {}'.format(i+1, l[i]))
print('AXIS:', a)