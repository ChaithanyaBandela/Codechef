# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    if (a*b)%4==0:
        print((a*b)//4)
    else:
        print((a*b)//4+1)