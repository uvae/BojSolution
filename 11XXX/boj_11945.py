n,m = map(int, input().split())
l = [input()[::-1] for _ in range(n)]
print(*l, sep='\n')