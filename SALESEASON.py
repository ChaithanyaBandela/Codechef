# cook your dish here
for i in range(int(input())):
    n=int(input())
    if n<=100:
        print(n)
    elif 100<n<=1000:
        print(n-25)
    elif 1000<n<=5000:
        print(n-100)
    elif(n>5000):
        print(n-500)