#include <iostream>
using namespace std;

int main() {
	// your code goes here
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
	    int sum=b;
	    for(int k=0;k<a;k++)
	    {
	        if(arr[k]<=sum)
	        {
	            cout<<"1";
	            sum=sum-arr[k];
	            
	        }
	        
	        else{
	            cout<<"0";
	        }
	    }
	    cout<<endl;
	}
	return 0;
}
