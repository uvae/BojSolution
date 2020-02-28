a,b = map(int, input().split())
(a,b) = (b,a) if a>b else (a,b)
print(b-a-1 if a!=b else 0); print(*[i for i in range(a+1,b)])