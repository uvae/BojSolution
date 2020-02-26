def hms2s(l): return l[0]*3600+l[1]*60+l[2]
e,s = hms2s(list(map(int, input().split(':')))), hms2s(list(map(int, input().split(':'))))
t = s-e if s-e>=0 else 86400+s-e
print('{:02d}:{:02d}:{:02d}'.format(t//3600, t%3600//60, t%60))