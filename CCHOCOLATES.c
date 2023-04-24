#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int x,y,z,a;
	    scanf("%d%d%d",&x,&y,&z);
	    a=5*x+10*y;
	    printf("%d\n",a/z);
	}
	return 0;
}

