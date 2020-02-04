l = [input() for _ in range(4)]
print('ignore' if l[0] in '89' and l[3] in '89' and l[1]==l[2] else 'answer')