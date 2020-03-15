y = [31,28,31,30,31,30,31,31,30,31,30,31]
w = ['Thursday','Friday','Saturday','Sunday','Monday','Tuesday','Wednesday']
d,m = map(int, input().split()); d += sum(y[0:m-1])-1
print(w[d%7])