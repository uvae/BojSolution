a,b = map(int, input().split()); A,B = a%4, b%4
print(abs((A if A else 4)-(B if B else 4))+abs((b//4+(1 if B else 0))-(a//4+(1 if A else 0))))