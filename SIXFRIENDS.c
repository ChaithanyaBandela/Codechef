#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int x,y;
	    scanf("%d%d",&x,&y);
	    if(3*x>2*y)
	    {
	        printf("%d\n",2*y);
	    }
	    else if(3*x<2*y)
	    {
	        printf("%d\n",3*x);
	    }
	    else
	    {
	        printf("%d\n",2*y);
	    }
	}
	return 0;
}

