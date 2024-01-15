#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,len, i,j,n;
    cin>>t;
    for(i=0;i<t;i++){
        cin>>len;
        char s[len];
        cin>>s;
        n=0;
        for(int j=0;j<len;j++){
            if(n<4){
            
                if((s[j]!='a' && s[j]!='e' && s[j]!='i' && s[j]!='o' && s[j]!='u')){
                   n++;
                }
                else{
                    n=0;
                }
            }
                
            
        }
        
        if(n>=4){
	        cout<<"NO"<<endl;
	   }else{
	     cout<<"YES"<<endl;
	   }
    }
	
	return 0;
}
