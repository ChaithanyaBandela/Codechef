# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    dis=x*100
    clo=y*10
    if dis==clo:
        print('Cloth')
    elif dis>clo:
        print('Cloth')
    else:
        print('Disposable')