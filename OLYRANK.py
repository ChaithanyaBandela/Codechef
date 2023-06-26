# cook your dish here
for i in range(int(input())):
    a,b,c,d,e,f=map(int,input().split())
    if(a+b+c>d+e+f):
        print('1')
    else:
        print('2')