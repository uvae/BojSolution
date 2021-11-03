import sys
from collections import deque

q = deque()
for _ in range(int(sys.stdin.readline())):
	l = sys.stdin.readline().split()
	
	if(l[0] == 'push_front'):
		q.appendleft(l[1])
	elif(l[0] == 'push_back'):
		q.append(l[1])
	elif(l[0] == 'pop_front'):
		print(q.popleft() if q else -1)
	elif(l[0] == 'pop_back'):
		print(q.pop() if q else -1)
	elif(l[0] == 'size'):
		print(len(q))
	elif(l[0] == 'empty'):
		print(1 if not q else 0)
	elif(l[0] == 'front'):
		print(q[0] if q else -1)
	elif(l[0] == 'back'):
		print(q[-1] if q else -1)
