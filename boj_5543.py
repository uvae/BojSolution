r, t, m = 0,0,2001

for i in range(3):
    t = int(input())
    if(t < m): m=t
    
r+=m
m = 2001

for i in range(2):
    t = int(input())
    if(t < m): m=t

print(r+m-50)
