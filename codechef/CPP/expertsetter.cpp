#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
    float a,b,c;
	cin>>t;
	for(int i=0;i<t;i++){
	    cin>>a>>b;
	    c=((b/a)*100);
        if(c<50){
            cout<<"NO"<<endl;
        }
        else{
            cout<<"YES"<<endl;
        }
	  
	}
	return 0;
}
