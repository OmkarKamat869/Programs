#include<iostream>
using namespace std;
void sort(int *c,int n)
{
    int a,b=0;
    a=c[0];
    for(int i=0;i<n;i++)
    {
        if(a<c[i])
        {
            a=c[i];
            
        }
        if(b<c[i] && c[i]<a)
                b=c[i];
    }   
    cout<<"2nd  "<<b;

}
int main()
{
    int x[10];
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {cin>>x[i];}
    sort(x,n);
    return 0;
}