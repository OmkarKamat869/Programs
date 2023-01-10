#include<stdio.h>
#include<math.h>
int main()
{
   int a[100],n,mean=0,i,b[100],sum=0;
   float sd;
   printf("E");
   scanf("%d",&n);
   printf("F");
   for(i=0;i<n;i++)
      scanf("%d",&a[i]);
   for(i=0;i<n;i++)
      mean+=a[i];
    mean/=n;
    for(i=0;i<n;i++)
      b[i]=pow(a[i]-mean,2);
    for(i=0;i<n;i++)
      sum+=b[i];
    sd=sqrt(sum/n);
    printf("sd=%f",sd);
    return 0;


}