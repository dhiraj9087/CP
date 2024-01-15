#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,a,b,c,d;
	cin>>t;
	for(int i=0;i<t;i++){
	    cin>>a>>b>>c>>d;
	    if((a*b)<=(c*d)){
	        cout<<"YES"<<endl;
	    }
	    else{
	        cout<<"NO"<<endl;
	    }
	}
	return 0;
}
