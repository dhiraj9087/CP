#include<iostream>
#include <math.h>
using namespace std;

class FD
{
    public:
    int fdno,month;
    float rate;
    int amt,mat_amt;
    string name;
   
    FD(float rt)
    {
        rate = rt;
    }
    
void accept()
{ 
   cout<<"Enter your FD number:"<<endl;
   cin>>fdno;
   cout<<"Enter your name:"<<endl;
   cin>>name;
   cout<<"Enter the amount:"<<endl;
   cin>>amt;
   cout<<"Enter the number of months:"<<endl;
   cin>>month;
   
}
void display()
{
    cout<<"Your FD number is:"<<fdno<<endl;
    cout<<"Your name is:"<<name<<endl;
    cout<<"The amount is:"<<amt<<endl;
    cout<<"The number of months:"<<month<<endl;
   
    
}
void matno()
{   float rt;
    double w;
    w =(1+(rate/100));
    mat_amt = amt * pow(w,month);
    cout<<"The maturity rate is :"<<mat_amt<<endl;
    
}
};
int main()
{
    FD s(10);
    s.accept();
    s.display();
    s.matno();
    
    return 0;
}