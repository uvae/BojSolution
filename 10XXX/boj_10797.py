n,r,l = int(input()), 0, list(map(int, input().split()))

for i in l:
    if(i%10 == n): r+=1

print(r)
