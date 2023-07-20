# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    x=107/100
    if x*a>=b:
        print('YES')
    else:
        print('NO')