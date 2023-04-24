#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int m,n,x,y,z;
	    scanf("%d%d%d",&m,&n,&x);
	    y=(2*m+2*n);
	    z=x*y;
	    printf("%d\n",z);
	}
	return 0;
}

