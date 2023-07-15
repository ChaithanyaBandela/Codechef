# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if (a+b)==1 or (b+c)==1 or (a+c)==1:
        print(1)
    else:
        print(0)