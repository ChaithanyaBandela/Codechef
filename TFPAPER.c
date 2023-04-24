#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int n,x;
	    scanf("%d%d",&n,&x);
	    printf("%d\n",n-x);
	}
	return 0;
}

