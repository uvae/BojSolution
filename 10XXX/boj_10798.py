l,r,m = [], '', 0
for i in range(5):
    t = input()
    if(len(t) > m): m=len(t)
    l.append( [len(t), t] )

for i in range(m):
    for s in l:
        if(s[0] > i): r+=s[1][i]

print(r)
