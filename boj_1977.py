l = [i*i for i in range(1,101)]; r = []
for i in range(int(input()), int(input())+1):
	if(i in l): r.append(i)
print(-1 if not(r) else '{}\n{}'.format(sum(r), min(r)))