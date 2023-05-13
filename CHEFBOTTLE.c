#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int n,x,k;
	    scanf("%d%d%d",&n,&x,&k);
	    if ( k/x <= n)
	    {
	        printf("%d\n",k/x);
	    }
	    else
	    {
	        printf("%d\n",n);
	    }
	}
	return 0;
}

