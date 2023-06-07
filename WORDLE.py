# cook your dish here
t=int(input())
an=' '
for i in range(t):
    s=list(input())
    p=list(input())
    for j in range(len(s)):
        if s[j]==p[j]:
            an+='G'
        else:
            an+='B'
    print(an)
    an=' '