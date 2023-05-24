# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    c=0
    for j in lst:
        if j>=10 and j<=60:
            c=c+1
    print(c)
