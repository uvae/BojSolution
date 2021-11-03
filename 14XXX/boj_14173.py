x1,y1,x2,y2 = map(int, input().split())
a1,b1,a2,b2 = map(int, input().split())
print(max(max(a2,x2)-min(a1,x1), max(b2,y2)-min(b1,y1))**2)