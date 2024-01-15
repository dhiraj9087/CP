#include<iostream>
using namespace std;

class Demo 
{
    int num;
    public:
    Demo ()
    {

    }
    Demo(int m)
    {
        num=m;
    }
    void output(){
        cout<<"value="<<num<<endl;
    }
};

int main()
{
    Demo r(10);
    r.output();

    Demo y=10;
    return 0;
}