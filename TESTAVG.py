# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if (a+b)/2 < 35:
        print('Fail')
    elif (a+c)/2 <35:
        print('Fail')
    elif (b+c)/2 <35:
        print('Fail')
    else:
        print('Pass')