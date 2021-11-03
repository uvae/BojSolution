n,f = int(input()[:-2]+'00'), int(input())
print('{:02d}'.format((f-n%f) if n%f else 0))