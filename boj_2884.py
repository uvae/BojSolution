n = list(map(int, input().split()))
n[0] -= 1
if(n[0] == -1): n[0]=23
n[1] += 15
if(n[1] > 60):
    n[0] +=1
    n[1] -= 60
if(n[0] == 24): n[0] = 0

print(n[0], n[1])
