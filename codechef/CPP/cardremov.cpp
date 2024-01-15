#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int a[n];
        int max = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        for (int j = 1; j <= 10; j++)
        {
            int sum = 0;
            for (int k = 0; k < n; k++)
            {
                if (a[k] == j)
                {
                    sum += 1;
                }
                if (sum > max)
                {
                    max = sum;
                }
            }
        }
        cout << n - max << endl;
        // int arr[n];
        // int foo=0;
        // for(int i=0;i<n;i++){
        //     cin>>a[i];
        // }
        // for(int j=0;j<=10;j++){
        //     int sum=0;
        //     if(a[j]==j){
        //         sum+=1;
        //     }
        //     arr[j]=sum;
        // }
        // for(int l=0;l<n;l++){
        //     if(arr[l]>foo){
        //         foo=arr[l];
        //     }
        // }
        // cout<<n-foo<<endl;
    }
    return 0;
}