n,l = int(input()),list(map(int, input().split()))
print(len(list(filter(lambda e: e+1!=l[e], [i for i in range(n)]))))