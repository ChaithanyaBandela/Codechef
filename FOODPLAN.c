#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int n,m;
	    scanf("%d%d",&n,&m);
	    if((n*0.9)<m)
	    {
	        printf("ONLINE\n");
	    }
	    else if((n*0.9)>m)
	    {
	        printf("DINING\n");
	    }
	    else
	    printf("EITHER\n");
	}
	return 0;
}

