n,g,e = int(input())+56,'0123456789','ABCDEFGHIJKL'
print(e[n%60%12]+g[n%60%10])