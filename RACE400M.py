# cook your dish here
for i in range(int(input())):
    x,y,z=map(int,input().split())
    al=400/x
    bo=400/y
    cha=400/z
    if al>bo and al>cha:
        print('ALICE')
    elif bo>al and bo>cha:
        print('BOB')
    else:
        print('CHARLIE')