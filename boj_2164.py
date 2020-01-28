# def c(n):
# 	l = [i for i in range(1, int(n)+1)]
# 	while len(l) != 1:
# 		l.append(l[1])
# 		del l[0:2]
# 	return l[0]
# print({i : c(i) for i in range(1, 100)})

l, n = [0, 1, 2, 2] + [0] * 499997, int(input())
for i in range(4, n+1):
	l[i] = l[i-1] + 2
	if(i-1 == l[i-1]): l[i] = 2
print(l[n])