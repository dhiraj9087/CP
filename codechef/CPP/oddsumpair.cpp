#include<iostream>
using namespace std;
int main()
{
int t;
cin>>t;
for(int i=0;i<t;i++)
{
    int a,b,c;
    cin>>a>>b>>c;
    if(a%2!=0)
    {
        if(b%2!=0)
        {
            if(c%2!=0)
            {
                cout<<"NO"<<endl;
            }
            else
            {
                cout<<"YES"<<endl;
            }
        }
        else
        {
            cout<<"YES"<<endl;
        }
    }
    
    else if(b%2!=0)
    {
        cout<<"YES"<<endl;
    }
    else if(c%2!=0)
    {
        cout<<"YES"<<endl;
    }
    
    else
    {
        cout<<"NO"<<endl;
    }


}
return 0;
}