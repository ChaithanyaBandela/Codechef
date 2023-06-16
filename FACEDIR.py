# cook your dish here
for _ in range(int(input())):
    a=int(input())
    if a%4==1:
        print('East')
    elif a%4==2:
        print('South')
    elif a%4==3:
        print('West')
    else:
        print('North')