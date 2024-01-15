#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,a,c;
	
	cin>>t;
	for(int i=0;i<t;i++){
	    cin>>a;
	    c=(a/4);
	    if(a%4==0){
	        cout<<c<<endl;
	    }
	    else{
	        cout<<c+1<<endl;
	    }
	}
	return 0;
}
