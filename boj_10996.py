n = int(input())
s = '{}\n{}'.format('* '*(n//2+(1 if n%2 else 0)), ' *'*(n//2))
for _ in range(n):
	print(s)