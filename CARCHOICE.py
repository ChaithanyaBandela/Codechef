# cook your dish here
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if c/a < d/b:
        print('-1')
    elif c/a==d/b:
        print('0')
    elif c/a > d/b:
        print('1')