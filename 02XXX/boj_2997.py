l = sorted(map(int, input().split()))
a,b = l[1]-l[0],l[2]-l[1]
print(l[-1]+a if a==b else l[-1]-a if b>a else l[0]+b)