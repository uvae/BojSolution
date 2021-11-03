a,b,c = map(int, input().split())
n = '+' if a+b == c else '-' if a-b == c else '*' if a*b == c else '/' if a/b == c else None
if(n): print('{}{}{}={}'.format(a,n,b,c))
n = None if n else '+' if a == b+c else '-' if a == b-c else '*' if a == b*c else '/' if a == b/c else None
if(n): print('{}={}{}{}'.format(a,b,n,c))
