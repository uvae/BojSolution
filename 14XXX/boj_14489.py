m = sum(map(int, input().split()))
p = int(input())
print(m if m<p*2 else m-p*2)