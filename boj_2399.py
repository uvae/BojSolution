# from sys import stdin
# input(); l,s = sorted(map(int, stdin.readline().split())),0
# for i in range(len(l)-1):
# 	for j in range(i, len(l)):
# 		s += l[j]-l[i]
# print(s*2)

input(); l = sorted(map(int, input().split()))
s,ll = 0,len(l)
for i in range(1, ll):
	s += (l[i]-l[i-1])*(ll-i)*i
print(s*2)