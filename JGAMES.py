# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    if (y-x)%2==0:
        print('Janmansh')
    else:
        print('Jay')