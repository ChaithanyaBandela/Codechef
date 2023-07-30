# cook your dish here
for i in range(int(input())):
    x,y,z=map(int,input().split())
    if (x+y)%2!=0:
        print('YES')
    elif (y+z)%2!=0:
        print('YES')
    elif(x+z)%2!=0:
        print('YES')
    else:
        print('NO')