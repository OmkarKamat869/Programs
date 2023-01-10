#include <stdio.h>
#include <stdlib.h>
#include<string.h>
void countalphadigits(char str[],int *pa,int *pd);
int main()
{
    char str[100];
    int cnta=0,cntd=0;
    scanf("%s",str);
    countalphadigits(str,&cnta,&cntd); //Parameters= str, &cnta, &cntd
    printf("%d,%d",cnta,cntd);
    return 0;
    
}


void countalphadigits(char str[],int *pa,int *pd)
{ int i;
  for(i=0;str[i]!='\0';++i)
  { if((str[i]>='A'&& str[i]<='Z')|| (str[i]>='a'&& str[i]<='z'))
     ++*pa;
    else if (str[i]>='0'&& str[i]<='9') 
     ++*pd;
    else
    {}
  }
  return;
}