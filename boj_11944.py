n,m = map(int, input().split())
print(str(n)*n if n<m else (str(n)*n)[:m])