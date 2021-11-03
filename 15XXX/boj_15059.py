l,c = list(map(int,input().split())), list(map(int,input().split()))
print(sum([c[i]-l[i] if c[i]>l[i] else 0 for i in range(3)]))