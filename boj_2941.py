s = input()
for i in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']: s = s.replace(i, ';')
print(len(s))