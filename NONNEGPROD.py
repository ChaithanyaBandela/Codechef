# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    A=list(map(int, input().split()))
    c=0
    p=1
    for k in range(n):
        p=p*A[k]
        
    if(p>=0):
        print(0)
    else:
        print(1)