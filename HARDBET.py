# cook your dish here
for i in range(int(input())):
    sub=list(map(int,input().split()))
    hard=min(sub)
    if hard is sub[2]:
        print('ALice')
    elif hard is sub[1]:
        print('Bob')
    else:
        print('Draw')