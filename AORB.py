# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=(500-(a*2))+(1000-((a+b)*4))
    e=(1000-(b*4))+(500-((a+b)*2))
    print(max(c,e))