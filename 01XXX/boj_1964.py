n, l = int(input()), [5, 7]
for i in range(1, n-1): l.append(l[i]+3)
print(sum(l[:n]) % 45678)