#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int A,B,C,D,E;
	    scanf("%d%d%d%d",&A,&B,&C,&D);
	    if(A > B+C+D || B > A+C+D || C > A+B+D || D > A+B+C)
	    {
	        printf("YES\n");
	    }
	    else
	    {
	        printf("NO\n");
	    }
	}
	return 0;
}

