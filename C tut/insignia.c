#include<stdio.h>
int main()
{  
   int n,k,i,j,x1,x2;
   int sum1 = 0 , sum2 = 0;
   printf("INSIGNIA\n");
   printf("Enter the number\n");
   scanf("%d",&n);
   for( k=1; k<=n; k++)
   {
       sum1 = sum1 + k;
   }
   printf("sum of the first n number is : %d\n",sum1);
     while(i < n/2)
   {
      x1 = x1 + i;
         i++;
    }
   for(int j=1; j<=n; j++)
   {
       sum2 = sum2 + j;
   }
   printf("sum of the another n number is: %d\n",sum2);
    while(i < n/2)
     {
        x2 = x2+i;
           i++;
     }
   if(sum1 == sum2)
   {
       printf("both numbers are equal\n");
       printf("winner");
   }
   return 0;
    
}