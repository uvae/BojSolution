s, c, n, l = 0, [0, 1] + [0]*99, input(), input().replace(' ', '').split('0')
for i in range(2, 101): c[i] = c[i-1] + i
for i in l: s += c[len(i)]
print(s)