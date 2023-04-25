#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int n,k;
	    scanf("%d%d",&n,&k);
	    if(n<k)
	    {
	        printf("Yes\n");
	    }
	    else if(n==k)
	    {
	        printf("NO\n");
	    }
	    else
	    {
	        printf("NO\n");
	    }
	}
	return 0;
}

