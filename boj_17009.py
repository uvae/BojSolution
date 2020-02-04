a, b = [int(input()) for _ in range(3)], [int(input()) for _ in range(3)]
a, b = a[0]*3 + a[1]*2 + a[2], b[0]*3 + b[1]*2 + b[2]
print('A' if a>b else 'B' if b>a else 'T')