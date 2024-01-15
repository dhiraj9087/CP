#include <iostream>
using namespace std;

int main()
{
    int a;
    cin >> a;
    while (a--)
    {
        int n;
    cin >> n;
    string s;
    cin >> s;
    string result;
    char c = s[0];
    for (int i = 1; i < n; i++)
    {
        if (s[i] == c)
        {
            result.push_back(s[i]);
            c = s[i + 1];
            i++;
        }
    }
    cout << result << endl;
    }
    return 0;
}