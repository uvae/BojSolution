n,b = map(int, input().split())
r,l='','0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while n: r += l[n%b]; n//=b
print(r[::-1])