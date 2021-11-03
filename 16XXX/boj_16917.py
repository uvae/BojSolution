a,b,c,x,y = map(int, input().split())
print(min(a*x+b*y,(x*2*c)+(y-x)*b if x<y else (y*2*c)+(x-y)*a,max(x,y)*2*c))