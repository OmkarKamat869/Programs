#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[100],n,i,max,min;
    printf("Enter the number of Elements= ");
    scanf("%d",&n);
    printf("Enter the Elements \n");
    for(i=0;i<n;++i)
      scanf("%d",&a[i]);
    max=a[0];
    min=a[0];
    for(i=1;i<n;++i)
    { 
        if(a[i]>max)
         max=a[i];
        if(a[i]<min)
          min=a[i];
    }
    printf("MAXIMUM=%d   MINIMUM=%d",max,min);
    return 0;
}
