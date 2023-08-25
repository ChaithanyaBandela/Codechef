# cook your dish here
for i in range(int(input())):
    B=list(map(int,input().split()))
    c=0
    for i in B:
        if(i==0):
            c+=1
    if(c>1):
        print("Water filling time")
    else:
        print("Not now")