#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
using namespace std;
typedef long long ll;
#define endl "\n"
const int mod = 1000000007;
const int N = 1e5 + 10;

void solve()
{
    ll n, q;
    cin >> n >> q;
    vector<ll> v(n);
    vector<ll> v2(q);
    for (auto &i : v)
    {
        cin >> i;
    }
    for (auto &j : v2)
    {
        cin >> j;
    }
    unordered_map<ll, ll> mp;
    for (ll i = 0; i < q; i++)
    {
        mp[v2[q - i - 1]]++;
    }
    for (auto &i : v)
    {
        for (auto &j : mp)
        {
            ll cmp = pow(2, j.first);
            if (i % cmp == 0)
            {
                cout << i << " " << j.first << endl;
                i += pow(2, j.first - 1);
            }
        }
    }
    for (auto &i : v)
    {
        cout << i << " ";
    }
    cout << endl;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}
