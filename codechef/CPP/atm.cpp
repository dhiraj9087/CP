#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int a,b;
        cin>>a>>b;
        int arr[a];
        for(int j=0;j<a;j++)
        {
            cin>>arr[j];
        }
        for(int k=0;k<a;k++)
        {
            cout<<arr[k];
        }
    }
}