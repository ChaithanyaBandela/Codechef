# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if (a+b)/2 > c:
        print('YES')
    else:
        print('NO')