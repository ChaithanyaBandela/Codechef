#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int x,sum=0,rem;
        scanf("%d",&x);
        while (x>0)
        {
            rem=x%10;
            sum=sum+rem;
            x=x/10;
        }
        printf("%d\n",sum);
    }
}