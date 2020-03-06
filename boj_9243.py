n = int(input())%2; a,b = input(),input()
if(n): a = ''.join(['1' if a[i]=='0' else '0' for i in range(len(a))])
print('Deletion succeeded' if a==b else 'Deletion failed')