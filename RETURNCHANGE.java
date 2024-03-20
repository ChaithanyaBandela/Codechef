import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		for(int i=0;i<t;i++){
		    int x=sc.nextInt();
		    int y=x%10;
		    int z=x/10;
		    int a=z*10;
		    if(y<5){
		        z=a;
		    }
		    else{
		        z=a+10;
		    }
		    System.out.println(100-z);
		}
	}
}
