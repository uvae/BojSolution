n,s = input(),0
s += 4 if 'A' in n else 3 if 'B' in n else 2 if 'C' in n else 1 if 'D' in n else 0
s += 0.3 if '+' in n else -0.3 if '-' in n else 0
print(float(s))