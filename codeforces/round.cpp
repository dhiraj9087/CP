#include <iostream>
using namespace std;


void solve()
{
    
    string str;
    cin >> str;
    int length = str.size();
    for (int i = length - 1; i > 0; i--)
    {
        if (str[i] >= '5')
        {
            str[i - 1]++;
        }
    }
    if (str[0] >= '5')
    {
        str = '1' + str;
    }

    int index = length + 2;
    for (int i = 0; i <= length; i++)
    {
        if (str[i] >= '5')
        {
            index = i;
            break;
        }
    }

    for (int i = index; i <= length; i++)
    {
        str[i] = '0';
    }
    cout << str << endl;
}

int main()
{
    
    int numTests;
    cin >> numTests;
    while (numTests--)
    {
        solve();
    }
    return 0;
}
