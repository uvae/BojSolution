n,a,b,c,d = map(int, input().split())
a,c = (n//a + (1 if n%a else 0))*b, (n//c + (1 if n%c else 0))*d
print(a if a<c else c)