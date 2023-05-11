#include <stdio.h>

int main(void) {
	// your code goes here
	int i,t,n,x;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
	    scanf("%d%d",&n,&x);
	    if(n%2==0)
	    {
	    if(x>=(n/2))
	    printf("yes\n");
	    else 
	    printf("no\n");
	    }
	    else
	    {
	        if(x>=(n/2)+1)
	    printf("yes\n");
	    else 
	    printf("no\n");
	    }
	    
	}
	return 0;
}
