n, sList = int(input()), [0]*246913

for i in range(2, 2*n+1, 1):
    if (sList[i] == 1): continue;
    for j in range(i*i, 2*n+1, i):
        sList[j] = j

print(sList[:50])
