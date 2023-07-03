# cook your dish here
chef=int(input())
for h in range(chef):
  a,b,c,d,e=map(int,input().split())
  if min(a/c,b/d)>=e:
    print("YES")
  else: print("NO")