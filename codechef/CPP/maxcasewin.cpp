#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
	    int a,b,c,d;
	    cin>>a>>b>>c>>d;
	    int x=max(a,b);
	    int y=max(c,d);
	    if(x<y)
	    cout<<"P"<<endl;
	    else if(x>y)
	    cout<<"Q"<<endl;
	    else 
	    cout<<"TIE"<<endl;
	}
	
	
	return 0;
}
