# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if a+b > c:
        print('TRAIN')
    elif a+b < c:
        print('PLANEBUS')
    else:
        print('EQUAL')