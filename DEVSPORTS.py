# cook your dish here
for _ in range(int(input())):
    Z,Y,A,B,C=map(int,input().split())
    if Z-Y<(A+B+C):
        print('NO')
    else:
        print('YES')