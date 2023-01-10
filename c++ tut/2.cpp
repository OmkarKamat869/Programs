#include<iostream>
using namespace std;
int max(int arr[],int m,int n)
{   int a=0;
    for(int i=m;i<=n;i++)
        if(a<arr[i])
            a=arr[i];
    return a;
}
void trapwater(int arr[],int n)
{   int trap=0;
    for(int i=1;i<n-1;i++)
    {
        int a=max(arr,0,i);
        int b=max(arr,i+1,n);
        if(b<a)
            a=b;
        if(a>arr[i])
        {
            trap+=(a-arr[i]);
        }

        
    }
    cout<<trap;
}



int main()
{
   int arr[5]={1,2,3,2,1};
   trapwater(arr,5);
}