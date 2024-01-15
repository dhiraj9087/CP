#include<iostream>
using namespace std;
int main() {
    int t;
    cin>>t;
    for(int j=0;j<t;j++)
    {
        int n,i,c=1;
        cin>>n;
        string s;
        cin>>s;
        for(i=1;i<n;i++){ 
            if(s[i]=='1')
            {
                c++;
            }
            else{
            break;
            }
        }
        cout<<c<<endl;
        
    }
  return 0;
}