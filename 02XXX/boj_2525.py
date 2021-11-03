s, b = map(int, input().split())
b += int(input()); s += b // 60; b %= 60; s %= 24
print(s, b)