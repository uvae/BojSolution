t = [int(input()) for _ in range(3)]
if(sum(t) != 180): print('Error')
elif(max(t)-min(t) == 0): print('Equilateral')
elif(t[0] != t[1] and t[1] != t[2] and t[0] != t[2]): print('Scalene')
else: print('Isosceles')