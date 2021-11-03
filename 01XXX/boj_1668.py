l = [int(input()) for _ in range(int(input()))]
p,c=0,0
for i in l:
	if(i>p): c+=1; p=i
print(c)
p,c=0,0
for i in l[::-1]:
	if(i>p): c+=1; p=i
print(c)