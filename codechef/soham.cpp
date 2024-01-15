#include<string>
#include<iostream>
#include<conio>
using namespace std;

class person
{
    private: char name[80]
    public: person()
    {
        strcpy (name,"bob"):
    }
    virtual void print()
    {
        cout<<"\nname of person through main objective is:"<<name;
    }
};
class student: public person
{
    private: char name_1[BO];
    public: student()
    {
        strcpy(name_1,"tom"):
    }
    void point()
    {
        cout<<"\nname of the person assigned thorugh derivative object:"<<name_1;

    }
};
void main()
{
    clrscr();
    person*n;x;
    student y;
    n=&x;
    n->print();
    n=&y;
    n->print();
    getch();
}
