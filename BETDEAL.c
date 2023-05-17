#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int x,y,a,b;
	    scanf("%d%d",&x,&y);
	    a=100-x;
	    b=200-(y*2);
	    if(a>b)
	    printf("SECOND\n");
	    else if(a==b)
	    printf("BOTH\n");
	    else
	    printf("FIRST\n");
	}
	return 0;
}

