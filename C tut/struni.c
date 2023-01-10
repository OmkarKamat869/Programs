#include<stdio.h>
struct struct_example
{
    int integer;
    float decimal;
    char name[20];
}s1;
  
// declaring union
  
union union_example
{
    int integer;
    float decimal;
    char name[20];
}u1;

int main()
{    

printf("%ld", sizeof(s1));
printf("%ld", sizeof(u1));

    return 0;
}