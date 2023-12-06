/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		for(int i=0;i<n;i++)
		{
		    int x=sc.nextInt(),N=sc.nextInt();
		    if(N%100==0)
		    {
		        if(N>(x*100)){
		            System.out.println((N/100)-x);
		        }
		        else{
		            System.out.println(0);
		        }
		    }
		    else{
		        if(N>x*100){
		            System.out.println(((N-(x*100))/100)+1);
		        }
		        else 
		            System.out.println(0);
		    }
		}
		
	}
}
