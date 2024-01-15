#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
	    int a,b,c,T,A,B,C;
	    cin>>a>>b>>c>>T>>A>>B>>C;
	    if(a<=A && b<=B && c<=C)
	    {
	        if(T<=(A+B+C))
	        {
	            cout<<"YES"<<endl;
	        }
	        else
	        {
	            cout<<"NO"<<endl;
	        }
	    }
	    else
	    {
	        cout<<"NO"<<endl;
	    }
	}
	return 0;
}
