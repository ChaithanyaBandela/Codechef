#include <stdio.h>

int main(void) {
    int t;
    scanf("%d",&t);
    while(t--){
        int a,b,c,d;
        scanf("%d %d %d %d",&a,&b,&c,&d);
        if(a+b>=d || a+c>=d || b+c>=d)
        printf("yes\n");
        else
        printf("no\n");
    }
	// your code goes here
	return 0;
}

