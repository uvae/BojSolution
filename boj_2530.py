s, b, c = map(int, input().split())
c += int(input()); b += c // 60; c %= 60; s += b // 60; b %= 60; s %= 24
print(s, b, c)