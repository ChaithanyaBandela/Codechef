# cook your dish here
for i in range(int(input())):
    x,y,a,b,k=map(int,input().split())
    p=x+k*a
    d=y+k*b
    if p<d:
        print('PETROL')
    elif d<p:
        print('DIESEL')
    else:
        print('SAME PRICE')