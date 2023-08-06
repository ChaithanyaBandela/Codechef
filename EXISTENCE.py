# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    lhs=pow(x,4)+4*y**2
    rhs=4*x**2*y
    if lhs==rhs:
        print('YES')
    else:
        print('NO')