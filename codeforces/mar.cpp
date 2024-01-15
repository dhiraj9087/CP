#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define endl "\n"
const int mod = 1000000007;
const int N = 1e5 + 10;

void solve()
{
    int n;
    cin >> n;

    vector<int> a(n);
    vector<int> b(n);
    vector<pair<int, int>> arr;

    for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
    }

    for (int i = 0; i < n; ++i)
    {
        cin >> b[i];
        arr.push_back({a[i] + b[i], i});
    }

    sort(arr.rbegin(), arr.rend());

    int ans1 = 0, ans2 = 0;

    for (int i = 0; i < n; ++i)
    {
        if (i % 2 == 0)
        {
            ans1 += (a[arr[i].second] - 1);
        }
        else
        {
            ans2 += (b[arr[i].second] - 1);
        }
    }

    cout << (ans1 - ans2) << endl;
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
