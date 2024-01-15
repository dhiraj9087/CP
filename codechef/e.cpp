#include <iostream>
#include<map>
using namespace std;
typedef long long ll;
#define mod 1000000007
#define endl "\n"

void solve()
{
    int n;
    cin >> n;
    map<int, int> mp;
    for (int i = 0; i < 2 * n; i++)
    {
        int x;
        cin >> x;
        mp[x]++;
    }
   
    for (int i = 0; i < 2 * n; i++)
    {
        if (mp[i] == 0)
        {
            cout << "YES" << endl;
            return;
        }
        if (mp[i] == 1)
        {
            cout << "NO" << endl;
            return;
        }
    }
    cout << "YES" << endl;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}