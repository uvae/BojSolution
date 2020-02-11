input();s,t=0,0
for i in map(int, input().split()):
	if(i==t): s+=1; t=(t+1)%3
print(s)