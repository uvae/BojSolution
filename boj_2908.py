def rv_int(x): return int(x[::-1])
a, b = map(rv_int, input().split())
print(a if a > b else b)