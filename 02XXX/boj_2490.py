a = ['D', 'C', 'B', 'A', 'E']

for i in range(3):
    n = input().split()
    t=0
    for i in n: t+=int(i)
    print(a[t])
