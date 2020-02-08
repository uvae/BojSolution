n,k = map(int, input().split())
print('YES' if n <= sum(map(lambda e: int(e)//2+(1 if int(e)%2 else 0), input().split())) else 'NO')