# cook your dish here
purchase=int(input())
for p in range(purchase):
  q,p=map(int,input().split())
  if q<1000: print(q*p)
  else: print((q*p)-(0.1*(q*p)))
  