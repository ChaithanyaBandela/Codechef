# cook your dish here
for i in range(int(input())):
    a,b,x,y=map(int,input().split())
    if a*b <=x*y:
        print('Yes')
    else:
        print('No')