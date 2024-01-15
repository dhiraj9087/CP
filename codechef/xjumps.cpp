#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
	    int a,b;
        int c,d,e;
	    cin>>a>>b;
	    c=(a/b);
	    d=(c*b);
	    e=(a-d);

	    cout<<(c+e)<<endl;
	    
	}
	return 0;
}
