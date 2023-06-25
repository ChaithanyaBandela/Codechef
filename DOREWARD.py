# cook your dish here
for i in range(int(input())):
    n=int(input())
    if n<=3:
        print('BRONZE')
    elif n>3 and n<=6:
        print('SILVER')
    elif n>6:
        print('GOLD')