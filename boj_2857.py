l = ''
for i in range(5):
	if(input().find('FBI') != -1): l += str(i+1)+' '
print(l if l else 'HE GOT AWAY!')