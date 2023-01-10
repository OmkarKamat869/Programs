#include<stdio.h>

struct distance
{
    int feet;
    int inch;
};

int main()
{
    
    struct distance d1, d2, sum;
    
    printf("Enter feet and inch of first distance: ");
    scanf("%d%d", &d1.feet, &d1.inch);
    printf("Enter feet and inch of second distance: ");
    scanf("%d%d", &d2.feet, &d2.inch);

    sum.inch = d1.inch + d2.inch;
    sum.feet = d1.feet + d2.feet;

    if(sum.inch>=12)
    {
        sum.feet += sum.inch/12;
        sum.inch %= 12;
    }
    printf("Sum is %d' %d''", sum.feet, sum.inch);
    return 0;
}