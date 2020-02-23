s,j,i = input(),0,0
for l in range(len(s)-2):
	j,i = j+1 if s[l:l+3]=='JOI' else j, i+1 if s[l:l+3]=='IOI' else i
print(j,i,sep='\n')