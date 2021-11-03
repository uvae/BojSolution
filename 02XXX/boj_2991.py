def cf(v,a,b,c,d): return (1 if v%(a+b)<=a and v%(a+b) else 0)+(1 if v%(c+d)<=c and v%(c+d) else 0)
a,b,c,d = map(int, input().split())
p,m,n = map(int, input().split())
print(cf(p,a,b,c,d),cf(m,a,b,c,d),cf(n,a,b,c,d),sep='\n')