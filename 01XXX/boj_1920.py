# c, l, c1 = input(), input().split(), input()
# for f in input().split():
# 	print(1 if l.count(f) else 0)
l, n1, l1, n2, l2 = {}, input(), input().split(), input(), input().split()
for i in l1: l[i] = 1
for i in l2: print(1 if i in l else 0)