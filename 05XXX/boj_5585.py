n,c = 1000 - int(input()), 0

while(n > 0):
    if(n-500 >= 0): n-=500
    elif(n-100 >= 0): n-=100
    elif(n-50 >= 0): n-=50
    elif(n-10 >= 0): n-=10
    elif(n-5 >= 0): n-=5
    else: n-=1
    c+=1

print(c)
