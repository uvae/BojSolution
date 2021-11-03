l,s = [0 for i in range(26)],0
for i in input(): l[ord(i)-97] += 1
for i in input(): l[ord(i)-97] -= 1
for i in l: s += abs(i)
print(s)